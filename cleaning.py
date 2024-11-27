"""
Description: This file contains functions that clean the data in the Motor_Vehicle_Collisions_-_Person_20241111.csv file in drafts to reverse any oopsies that may have been made.
"""
def open_data(): 
    """
    Fruitful function that opens the Motor_Vehicle_Collisions_-_Person_20241111.csv file and reads the contents of the file. 
    Then splits it into separate records.
    """
    try:
        with open("Motor_Vehicle_Collisions_-_Person_20241111.csv", "r") as file: #opens the file
            contents = file.read() 
            lines = contents.splitlines()
            columns = [line.split(",") for line in lines]
            data = columns
            return data
    except FileNotFoundError:
        print("Error: The file 'Motor_Vehicle_Collisions_-_Person_20241111.csv' was not found.")

def clean_data():
    """
    Void function that cleans the data by removing the rows with "U" or "" in the PERSON_SEX column.
    """
    #opens the data
    data = open_data()
    #prep list for the clean data
    cleaned_data = []

    #header 
    header = data[0]

    Person_Sex_Index = header.index("PERSON_SEX")

    for row in data[1:]:
        if row[Person_Sex_Index] == "U" or row[Person_Sex_Index] == "":
            del row 
        else:
            cleaned_data.append(row)

    with open("cleaned_data_draft1.csv", "w") as file:
        file.write(",".join(header) + "\n")
        for row in cleaned_data:
            file.write(",".join(row) + "\n")

def person_injury_clean():
    """
    VOid function that cleans the data by removing the rows with "Unspecified" in the PERSON_INJURY column.
    """
    try:
        cleaned_data = []

        with open("cleaned_data_draft1.csv", "r") as file:
            contents = file.read()
            lines = contents.splitlines()
            columns = [line.split(",") for line in lines]
            data = columns 
    
        header = data[0]
        Person_Injury_Index = header.index("PERSON_INJURY")

        for row in data[1:]:
            if row[Person_Injury_Index] == "Unspecified":
                del row
            else:
                cleaned_data.append(row)

        with open("cleaned_data_draft2.csv", "w") as file:
            file.write(",".join(header) + "\n")
            for row in cleaned_data:
                file.write(",".join(row) + "\n")

    except FileNotFoundError:
        print("Error: The file 'cleaned_data_draft1.csv' was not found.")


clean_data()

person_injury_clean()