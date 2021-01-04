import numpy as np
import pandas as pd 

# Reading a local csv file with pd.read_csv()
frame = pd.read_csv('file.csv')
print(frame)

# CSV file is just a text file with comma-separated values
# So we can use pd.read_table() with delimiter=","
table = pd.read_table("file.csv", sep=",")
# or use the option delimiter=","
print(table)


# Pandas automatically assumes 
# the first line of the csv to be the header, 
# i.e, the table header
# But not all csv files have a header line
print("====================================")
print("This csv file has no header")
print(pd.read_csv("no_header.csv"))

# To prevent pandas from assuming 
# the first line to be the table header
# you can specify header=None when you read the file
# And pandas will assign number indices from 0, 
# like list indices as the table header
frame_1 = pd.read_csv("no_header.csv", header=None)
print(frame_1)

# Or, you can specify column names 
# with option names=[] when reading the csv
# names options takes in a list of labels
frame_1 = pd.read_csv("no_header.csv", 
                       names=["white", "red", 'blue', "green", "animal"])
print(frame_1) 


# Sometimes, you need a DataFrame 
# with hierarchicalstructure by reading a CSV file
# you can use index_col= option,
# assigning all the columns to be converted into indexes.
multi_level = pd.read_csv("multi_level.csv")

# To use hiearchical indexing, use index_col=
# option to specify the names of the multi-level 
# index columns
multi_level = pd.read_csv("multi_level.csv",
    index_col=['color', 'status']
)

print(multi_level)
