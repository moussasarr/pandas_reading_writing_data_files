import numpy as np
import pandas as pd 

# Writing a DataFrame object into a csv file
data = pd.DataFrame(np.arange(16).reshape(4, 4), 
       index=['red', 'blue', 'yellow', 'white'],
       columns=["ball", "pen", "pencil", "paper"]
       )

data.to_csv("data.csv")


# if you do not want the default pandas behavior of including 
# header and indexes,
data.to_csv("data_with_no_labels.csv", header=False, index=False)


# np.nan values in Data show as empty fields in csv
frame = pd.DataFrame([[6, np.nan, np.nan, 4 ],
                     [np.nan, 0, 2, np.NaN],
                     [np.nan, np.nan, 2, np.NaN],
                     [np.nan, np.nan, np.nan, np.NaN]],
                     index = ["black", "white", "red", "yellow"],
                     columns = ["bottle", "computer", "pone", "tv"]
                    )
frame.to_csv("nan.csv")


# You can also replace the empty filds using na_rep= option
# Usually we replace them with 0 or with NaN
frame.to_csv("na_rep.csv", na_rep="0")





