# tfrrs
A basic package that parses tfrrs cross country results and downloads tables on the page into a series of csv files.

Use of the package once installed is:

tfrrs -m [name of meet for filenaming] [tfrrs meet number] --men --women --individual --team --all

Where the meet number can be found at the end of a URL: https://www.tfrrs.org/results/xc/ [**meet number**] .html

For example, to get the men's team results from the 2016 Wisconsin Nuttycombe Invitational:

The results are located at: https://www.tfrrs.org/results/xc/**9718**.html

tfrrs -m wisco 9718 --men --team

team/individual/men/women filtering will sometimes miss results or mislabel them. The --all flag bypasses all attempts to filter the tables, and is recommended if you are experiencing issues however filenaming will always try to identify the type of results being downloaded.

Another way to download meets is to create a .txt file with each line having a meet name and meet number separated by a comma.

first meet name,first meet number
second meet name, second meet number
etc.

And running a command like:

tfrrs -f [meets.txt] --women --individual
