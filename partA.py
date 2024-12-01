#Author: Hareen Dimanka Sirisena
#Date: 21/11/2024
#Student ID: 20244020

# Task A: Input Validation
def validate_date_input():
    """
    Prompts the user for a date in DD MM YYYY format, validates the input for:
    - Correct data type
    - Correct range for day, month, and year
    """
    while True:
        try:
            while True: #Infinity loop to get the answer until it is true
            
                day = input("Please enter the day of the servey in the format dd: ") #Get the date input from user
                if not day.isdigit(): # if input is not a digit prints "Integer required" and continue to the begining
                    print("Integer required")
                    continue
                day = int(day) #Converts to an integer
                if day > 31 or day < 1: #Checks the values are within the range and if not continue to the top
                    print("Out of range, 01-31 for day")
                    continue
                break

            while True:
                    
                month = input("Please enter the month of the survey in the format MM: ")#Get the date input from user
                if not month.isdigit(): #if input is not a digit prints "Integer required" and continue to the begining
                    print("Integer required")
                    continue
                month = int(month)
                if month > 12 or month < 1:
                    print("Out of range, values must be in the range 1 to 12 ")
                    continue
                break
                
            while True:
                
                year = input("Please enter the year of the survey in the format YYYY: ")#Get the date input from user
                if not year.isdigit(): #if input is not a digit prints "Integer required" and continue to the begining
                    print("Integer required")
                    continue
                year = int(year) #Converts to an integer
                if year > 2024 or year < 2000: #Checks the values are within the range and if not continue to the top
                    print("Out of range, values must range from 2000 and 2024 ")
                    continue
                break
            return day, month, year #return the correct input as a tuple
            
        except Exception as error: #handles any errors apart from the above errors
            print(f"Error occured {error}")
            

def validate_continue_input():
    """
    Prompts the user to decide whether to load another dataset:
    - Validates "Y" or "N" input
    """
    
    while True:
        #Ask the user for another dataset and converts any lowercase to uppercase if lowercase is inserted
        #And uses strip to handle incase of any accidental leading spaces
        user_input = input("Do you need another dataset from the survey? (Y/N) : ").strip().upper()
        if user_input == "Y": #Checks the input of the user
            return True
        elif user_input == "N":
            return False
        else:
            print("Invalid. Enter 'Y' for yes or 'N' for no ")
            
if __name__ == "__main__":
    while True:
        date = validate_date_input()
        print(f"Date entered : {date[0]:02d}/{date[1]:02d}/{date[2]:02d}") # prints the date in DD/MM/YYYY format
        if not validate_continue_input(): 
            break 
    
   


# Task B: Processed Outcomes
def process_csv_data(file_path):
    """
    Processes the CSV data for the selected date and extracts:
    - Total vehicles
    - Total trucks
    - Total electric vehicles
    - Two-wheeled vehicles, and other requested metrics
    """
    pass  # Logic for processing data goes here

def display_outcomes(outcomes):
    """
    Displays the calculated outcomes in a clear and formatted way.
    """
    pass  # Printing outcomes to the console


# Task C: Save Results to Text File
def save_results_to_file(outcomes, file_name="results.txt"):
    """
    Saves the processed outcomes to a text file and appends if the program loops.
    """
    pass  # File writing logic goes here

# if you have been contracted to do this assignment please do not remove this line

