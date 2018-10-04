from os.path import basename, normpath

import matplotlib.pyplot as plt
from build_pew_verygeneral import read_data


def plot(file1, file2):
    """Plot two spectra"""
    wav1, flux1 = read_data(file1)
    wav2, flux2 = read_data(file2)

    # Incase you need a vertical offset (or lack of one)
    offset = 0

    plt.figure()
    plt.plot(wav1, flux1, label=basename(normpath(file2)))
    plt.plot(wav2, flux2 + offset, label=basename(normpath(file2)))

    # x and y limits
    # plt.xlim([x1,x2])
    # plt.ylim([y1,y2])
    plt.show()


if __name__ == "__main__":

    # Put your two file names here ""
    file1 = ""
    file2 = ""

    plot(file1, file2)
