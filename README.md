Python scripts for the Research Seminar

Descriptions about each python script (for more detailed explanations about specific parts of the codes, ask me):

1) build_pew_general.py : by running it in the terminal, having typed next to it the name of the star's fits-file and the two values of the wavelength range (line list), which the user wants to examine, it creates the spectrum, it recognizes the absorption line that exists in the defined range by finding the local minimum and the local maxima of the spectrum within this range, it defines and calculates the area between the pseudo-continuum and the flux (pseudo EW), while showing the plot of this absorption line with the EW fitted and marked. It's important use is that the user can actually verify the area that is calculated as EW for any line of any star and verify the precision of the measurement.

2) build_pew_verygeneral.py : it does the same process as the "general"-script, but it is designed in such a way so not to ask about specific fits-file and wavelength values before running it, but to able to be imported in the pew_multiplelines.py, so to calculate automatically all the EWs for all the absorpion lines for all the stars examined. This is the core-script that creates my results for the EWs.

3) pew_multiplelines.py : By running this, connected with (2), the user gets as outcome files that contain the EW values of each star, based on the line list used.

4) central_lines.py : this small script creates a list of the absorption lines, based on the wavelength ranges that was initially given for the calculations of EWs. It is used in several cases below, as I refer to an absorption line with it's central length-value (because the initial line list just contained the left and the right edges of it)

5) 
