#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:22:52 2017

@author: aantoniadis, jason-neal
"""

import multiprocess as mprocess
import numpy as np
from astropy.io import fits

from build_pew_verygeneral import read_data


def wav_selector(wav, flux, wav_min, wav_max):
    """Wavelength selector.

    Slice array to within wav_min and wav_max inclusive.
    """
    assert not (np.isnan(wav_min)), "Lower wavelength band is NaN!"
    assert not (np.isnan(wav_max)), "Upper wavelength band is NaN!"

    wav = np.asarray(wav)
    flux = np.asarray(flux)

    # Remove NaN wavelengths
    nan_mask = np.isnan(wav)
    wav = wav[~nan_mask]
    flux = flux[~nan_mask]
    assert not np.any(np.isnan(wav))
    mask = (wav >= wav_min) & (wav <= wav_max)
    wav_sel = wav[mask]
    flux_sel = flux[mask]
    return wav_sel, flux_sel


def unitary_Gauss(x, center, fwhm):
    """Gaussian_function of area=1.

    p[0] = A;
    p[1] = mean;
    p[2] = full with at half maximum (fwhm);
    """
    sigma = np.abs(fwhm) / (2 * np.sqrt(2 * np.log(2)))
    Amp = 1.0 / (sigma * np.sqrt(2 * np.pi))
    tau = -((x - center) ** 2) / (2 * (sigma ** 2))
    result = Amp * np.exp(tau)

    return result


def fast_convolve(wav_val, R, wav_extended, flux_extended, fwhm_lim):
    """IP convolution multiplication step for a single wavelength value."""
    fwhm = wav_val / R
    # Mask of wavelength range within 5 fwhm of wav
    index_mask = (wav_extended > (wav_val - fwhm_lim * fwhm)) & (
        wav_extended < (wav_val + fwhm_lim * fwhm)
    )

    flux_2convolve = flux_extended[index_mask]
    # Gaussian Instrument Profile for given resolution and wavelength
    inst_profile = unitary_Gauss(wav_extended[index_mask], wav_val, fwhm)

    sum_val = np.sum(inst_profile * flux_2convolve)
    # Correct for the effect of convolution with non-equidistant positions
    unitary_val = np.sum(inst_profile * np.ones_like(flux_2convolve))

    return sum_val / unitary_val


def wrapper_fast_convolve(args):
    """Wrapper for fast_convolve.

    Needed to unpack the arguments for fast_convolve as multiprocess.Pool.map does not accept multiple
    arguments.
    """
    return fast_convolve(*args)


def ip_convolution(
    wav, flux, chip_limits, R, fwhm_lim=5.0, numProcs=None):
    """Spectral convolution which allows non-equidistant step values.

    Parameters
    ----------
    wav:
        Wavelength
    flux:
        Flux of spectrum
    chip_limits: List[float, float]
        Wavelength limits of region to return after convolution.
    R:
        Resolution to convolve to.
    fwhm_lim:
        Number of FWHM of convolution kernel to use as edge buffer.
    numProcs: int
        NUmber of processes to use. Default=None selects cpu_count - 1.
     """
    # Turn into numpy arrays
    wav = np.asarray(wav, dtype="float64")
    flux = np.asarray(flux, dtype="float64")

    wav_chip, flux_chip = wav_selector(wav, flux, chip_limits[0], chip_limits[1])
    # We need to calculate the fwhm at this value in order to set the starting
    # point for the convolution
    fwhm_min = wav_chip[0] / R  # fwhm at the extremes of vector
    fwhm_max = wav_chip[-1] / R

    # Wide wavelength bin for the resolution_convolution
    wav_min = wav_chip[0] - fwhm_lim * fwhm_min
    wav_max = wav_chip[-1] + fwhm_lim * fwhm_max
    wav_ext, flux_ext = wav_selector(wav, flux, wav_min, wav_max)

    # Multiprocessing part
    if numProcs is None:
        numProcs = mprocess.cpu_count() - 1

    mprocPool = mprocess.Pool(processes=numProcs)

    args_generator = [[wav, R, wav_ext, flux_ext, fwhm_lim] for wav in wav_chip]


    flux_conv_res = np.array(mprocPool.map(wrapper_fast_convolve, args_generator))

    mprocPool.close()

    return wav_chip, flux_conv_res


def save_new_data(fname, flux, hdr):
    fits.writeto(fname, flux, hdr, overwrite=True)


if __name__ == "__main__":

    filepaths = np.loadtxt("filelist.dat", dtype=str)

    wavelength_range = np.loadtxt("lines.rdb", skiprows=2)

    R = 50000

    for fname in np.arange(len(filepaths)):
        wav, flux = read_data(fname)
        hdr = fits.getheader(fname)

        wav_limits = [wav[0], wav[-1]]
        convolved_wav, convolved_flux = ip_convolution(
            wav, flux, wav_limits, R, fwhm_lim=5.0
        )

        newname = fname.replace(".fits", "") + "new_resolution.fits"
        save_new_data(newname, convolved_flux, hdr)
