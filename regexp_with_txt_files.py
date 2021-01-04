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
