Python scripts for the Research Seminar

Descriptions about each python script (for more detailed explanations about specific parts of the codes, ask me):

1) build_pew_general.py : by running it in the terminal, having typed next to it the name of the star's fits-file and the two values of the wavelength range (line list), which the user wants to examine, it creates the spectrum, it recognizes the absorption line that exists in the defined range by finding the local minimum and the local maxima of the spectrum within this range, it defines and calculates the area between the pseudo-continuum and the flux (pseudo EW), while showing the plot of this absorption line with the EW fitted and marked. It's important use is that the user can actually verify the shape of area that is calculated as EW for any line of any star and verify the precision of the measurement.

2) build_pew_verygeneral.py : it does the same process as the "general"-script, but it is designed in such a way so not to ask about specific fits-file and wavelength values before running it, but to able to be imported in the pew_multiplelines.py, so to calculate automatically all the EWs for all the absorpion lines for all the stars examined. This is the core-script that creates my results for the EWs.

3) pew_multiplelines.py : By running this, connected with (2), the user gets as outcome files that contain the EW values of each star, based on the line list used.

4) central_lines.py : this small script creates a list of the absorption lines, based on the wavelength ranges that was initially given for the calculations of EWs. It is used in several cases below, as I refer to an absorption line with it's central length-value (because the initial line list just contained the left and the right edges of it)

5) saveVascoEW.py : This script saves the measurements of EWs as occured by Vasco's code, and creates the respective files with the appropriate name for each star. 

6) Do_Correlation.py : This script firstly correlates the stars/names of my EW-files with the respective files of Vasco, in order to be able to identify which star/file with my EWs should be compared and plotted with its pair from Vasco EW files that I had saved with the scipt (5), since the EW files of the stars were originally saved with different names, because I needed to distinguish which of those contain my results and which ones are Vasco results. Then, for each star ,figures with my values of EWs are plotted against Vasco's values of the respective EWs, including also the slope so to see how good the matching is.

7) Difference_Correlation.py : This script follows the same correlation process as in (6), and then it plots the difference of EWs, including the mean, median and standard deviation of the difference for each star, which are shown as lines on the data and in a box with their values. Furthermore, the script saves these statistical values to a seperate csv file, along with the metallicity and temperature values of each star as calculated by Vasco.

8) Relative_Difference_Correlation.py : This script is similar to (7) but gives the % difference of my and Vasco measurements, considering as "theoretical" reference value the measurements of Vasco.

9) CDscript.py : This script creates the "tableCD" that contains the (AA-VN) differences of EWs (similarly correlated as above) for every absorption line (vertically) for every star (horizontally). This table is used in the following scripts , in order to create the "C plots" and "D plots" as explained there.

10) rel_CDscript.py : The same purpose as in (9) but for the relative differences, meaning the % differences.

11) 









