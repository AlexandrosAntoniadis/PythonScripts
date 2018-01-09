Python scripts for the Research Seminar

Descriptions about each python script (for more detailed explanations about specific parts of the codes, ask me):

1) build_pew_general.py : by running it in the terminal, having typed next to it the name of the star's fits-file and the two values of the wavelength range (line list), which the user wants to examine, it creates the spectrum, it recognizes the absorption line that exists in the defined range by finding the local minimum and the local maxima of the spectrum within this range, it defines and calculates the area between the pseudo-continuum and the flux (pseudo EW), while showing the plot of this absorption line with the EW fitted and marked. It's important use is that the user can actually verify the shape of area that is calculated as EW for any line of any star and verify the precision of the measurement.

2) build_pew_verygeneral.py : it does the same process as the "general"-script, but it is designed in such a way so not to ask about specific fits-file and wavelength values before running it, but to able to be imported in the pew_multiplelines.py, so to calculate automatically all the EWs for all the absorpion lines for all the stars examined. This is the core-script that creates my results for the EWs.

3) pew_multiplelines.py : By running this, connected with (2), the user gets as outcome files that contain the EW values of each star, based on the line list used.

4) central_lines.py : this small script creates a list of the absorption lines, based on the wavelength ranges that was initially given for the calculations of EWs. It is used in several cases below, as I refer to an absorption line with it's central length-value (because the initial line list just contained the left and the right edges of it)

5) saveVascoEW.py : This script saves the measurements of EWs as occured by Vasco's code, and creates the respective files with the appropriate name for each star. 

6) Do_Correlation.py : This script firstly correlates the stars/names of my EW-files with the respective files of Vasco, in order to be able to identify which star/file with my EWs should be compared and plotted with its pair from Vasco EW files that I had saved with the scipt (5), since the EW files of the stars were originally saved with different names, because I needed to distinguish which of those contain my results and which ones are Vasco results. Then, for each star ,figures with my values of EWs are plotted against Vasco's values of the respective EWs, including also the slope so to see how good the matching is.

7) Difference_Correlation.py : This script follows the same correlation process as in (6), and then it plots the difference of EWs, including the mean, median and standard deviation of the difference for each star, which are shown as lines on the data and in a box with their values. Furthermore, the script saves these statistical values to a seperate csv file, along with the metallicity and temperature values of each star as calculated by Vasco. This "statistical study" file will be needed at the "C_plot.py" script where I correlate and plot the temperature of each star against its average EW difference in the two methods.

8) Relative_Difference_Correlation.py : This script is similar to (7) but gives the % difference of my and Vasco measurements, considering as "theoretical" reference value the measurements of Vasco.

9) CDscript.py : This script creates the "tableCD" that contains the (AA-VN) differences of EWs (similarly correlated as above) for every absorption line (vertically) for every star (horizontally). This table is used in the following scripts , in order to create the "C plots" and "D plots" as explained there.

10) rel_CDscript.py : The same purpose as in (9) but for the relative differences, meaning the % differences.

11) C_plot.py : This script creates "EW differences VS Teff" diagrams for each line individualy (4104 plots with 112 points/stars each). This kind of diagrams, apart from being test for my EW-calculation method, also tell us how more easy/difficult is to measure each individual line for hotter/cooler stars (bigger difference --> more difficult)

12) rel_Cplot.py : the purpose of (11) may be more clear to conclude by looking at the % difference in measurements each individual line has according to the temperature of the star. 

13) D_plot.py :  This creates a "mean differences (each of them is an average of 112 values) VS absorption lines" diagram to show how the average values of the corresponding EW differences relate to their respective wavelengths. This diagram, again not only is a test for my method compared to Vasco method, but furthermore shows which absorption lines are difficult to be
measured regardless the star and temperature and how many are measured accurately. In this case, I am able to spot directly which lines have the big offset.

14) zoom_Dplot.py : Because of the fact that very few lines (not more than 5) had big differences, I prefer to see more clearly the remaining huge majority of the lines how they behave regarding the different methods, so I create a new plot zoomed in +/- 20 difference.

15) rel_Dplot.py : similar with (13) but for the % average difference.

16) rel_zoom_Dplot.py : similar concept as in (14), and connected to the (15). I present the plot with the lines that have a +/- 100 % difference in the average values of EWs by me and Vasco. I consider this figure that occurs from this code, as the most important one among the figures occuring from (13), (14) and (15). 
( Using a mapping code that I will add to github later on, I see that the lines with difference greater than +/-15% are only around 70 out of 4014, which means that my method of calculating the pseudo-EWs works great and in a very good agreement with Vasco's.)

17) TeffVSmeandiff.py : this script creates a plot showing the mean difference on EW calculations of each star against its temperature, to see how small or big this is according to how cool or hot it is and reveal any trends about this possible connection.

18) Teff_VS_relativemeandiff.py : similar concept to (17), but more important, because it refers to the % mean difference, which gives a better understanding of the accuracy of measurements. The conclusions from this figure are more clear and solid.












