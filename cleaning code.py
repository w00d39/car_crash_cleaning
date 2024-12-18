import pandas as pd

#creates dataframe from csv file
df = pd.read_csv("C:/Users/apgod/Downloads/cleaned_data_draft2.csv")
#drop bicyclist values in person_type column
df=df[df['PERSON_TYPE'] != 'Bicyclist']
#drops rows with missing values in the columns VEHICLE_ID and EJECTION
df.dropna(subset=["VEHICLE_ID", "EJECTION"], inplace=True)
#drop useless columns
df.drop(columns=['PED_ACTION'])
#selects the first 400 rows of the dataframe
df_subset = df.head(400)
#saves the first 400 rows of the dataframe to a new csv file
df_subset.to_csv("cleaned_file.csv", index=False)
