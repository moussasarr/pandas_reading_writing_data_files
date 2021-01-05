import numpy as np
import pandas as pd

# sometimes you are only in processing a file into portions
# This is usually the case when working with large files
# you often need to read them into partions
# as you might not be intersted in parsing the entire file
# in this case you can use a combination of skiprows and nrows
# nrows specifies the number of rows of file to read

skipped = pd.read_table("file.csv", skiprows=[2], nrows=3, sep=",")
print(skipped)

# Sometimes you want to split text into portions
# you then apply some logic to each potion to process
# i.e, a specific operation is carried out on each portion

# Example, you want to extract the values in column, 
# once every 3 rows to insert the sums
# use the chunksize option
output = pd.Series()
pieces = pd.read_csv("file.csv", chunksize=3)

i = 0
for piece in pieces:
    output.at[i] = piece["white"].sum()
    i += 1

print(output)