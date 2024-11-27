import pandas as pd

#creates dataframe from csv file
df = pd.read_csv("C:/Users/apgod/Downloads/cleaned_data_draft2.csv")
#drops rows with missing values in the columns VEHICLE_ID and EJECTION
df.dropna(subset=["VEHICLE_ID", "EJECTION"], inplace=True)
#selects the first 400 rows of the dataframe
num_rows = 400
#saves the first 400 rows of the dataframe to a new csv file
df.to_csv("cleaned_file.csv", index=False, nrows=num_rows)