import numpy as np
import pandas as pd 

# Some we have space separated data in a text file
# Format is almost like a csv but space-separated
# or tab-seperated instead of comma-separated 
# we can use read_table() for text files with tabular data 
# and regular expressions to account for the space
# as separator
frame = pd.read_table("simple_file.txt", sep="\s+", engine="python")
print(frame)

# In some cases, separators can be characters such as alphanumeric, 
# In many cases, you might want to just extract the numbers part
# of a data file
numeric_data_frame = pd.read_table("mixed_alpha_numeric.txt", 
                                    sep="\D+", header=None,
                                    engine="python"
                                   )
print(numeric_data_frame)


# Sometimes we want to exclude some lines from parsing
# if you do not want to include some headers or 
# unnecessary comments and information
# in such cases, you can use the skiprows= option

# Ex1: we want to skip the first 5 rows, 
#  then use the option skiprows = 5
# Ex2: We want to skip a specific rows, like row 5
#  then use the skiprows option with a list, skiprows = [5]
log_table = pd.read_table("log_file.txt", skiprows=[0, 1, 3, 6], sep=",")
print(log_table)

