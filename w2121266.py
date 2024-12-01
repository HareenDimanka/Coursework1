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

    while True: # infinite loop to the entire input validation process until the correct input is entered
        try:
            while True: #Infinity loop to get the correct input for the day
            
                day = input("Please enter the day of the servey in the format dd: ") #Get the date input from user
                if not day.isdigit(): # if input is not a digit prints "Integer required" and continue to the begining
                    print("Integer required")
                    continue
                day = int(day) #Converts to an integer
                if day > 31 or day < 1: #Checks the values are within the range and if not continue to input day again
                    print("Out of range, 01-31 for day") #prints the error message
                    continue
                break # exit the loop if the day_input is correct

            while True: # Start an infinite loop again to get the correct correct input for the month
                    
                month = input("Please enter the month of the survey in the format MM: ")#Get the date input from user
                if not month.isdigit(): #if input is not a digit prints "Integer required" and continue to the begining
                    print("Integer required") #prints the error message
                    continue
                month = int(month) #converts string to int
                if month > 12 or month < 1: #check the value is within the range else continue to the top
                    print("Out of range, values must be in the range 1 to 12 ")
                    continue
                break # exit the loop if the input is correct
                
            while True: # Start an infinite loop again to get the correct correct input for the year
                
                year = input("Please enter the year of the survey in the format YYYY: ")#Get the date input from user
                if not year.isdigit(): #if input is not a digit prints "Integer required" and continue to the begining
                    print("Integer required")
                    continue
                year = int(year) #Converts to an integer
                if year > 2024 or year < 2000: #Checks the values are within the range and if not continue to the top
                    print("Out of range, values must range from 2000 and 2024 ") 
                    continue
                break # exit the loop if the input is correct
            return day, month, year #return the correct input as a tuple
            
        except Exception as error: #handles any errors apart from the above errors
            print(f"Error occured {error}") #prints the error message
        

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
        elif user_input == "N": #Checks for the user's input
            return False
        else:
            print("Invalid. Enter 'Y' for yes or 'N' for no ") # prints the error message
            

    pass  # Validation logic goes here


# Task B: Processed Outcomes  
import csv
from collections import defaultdict


def process_csv_data(file_path, selected_date):
    """
    Processes the CSV data for the selected date and extracts:
    - Total vehicles
    - Total trucks
    - Total electric vehicles
    - Two-wheeled vehicles, and other requested metrics
    """

    outcomes = { #initialize a dictionary with the following keys and values
        # Initialize variables
        "total_vehicles" : 0,
        "total_trucks" : 0,
        "total_electric_vehicles" : 0,
        "total_two_wheeled" : 0,
        "total_busses_north" : 0,
        "total_no_turn" : 0,
        "total_over_speed_limit" : 0,
        "total_elm_avenue" : 0,
        "total_hanley_highway" : 0,
        "total_scooters_elm_avenue" : 0,
        "hourly_vehicles_hanley_highway" : [0] * 24,
        "total_rain_hours" : 0,
        "total_bicycles" : 0 
    }

    try:
        with open(file_path, mode = 'r') as file: #opens the csv file and read its content 
            reader = csv.DictReader(file)
            for row in reader: # iterate through each row of the csv file checking if the date matches the selected date
                if row['Date'] != selected_date:
                    continue
                outcomes["total_vehicles"] += 1 # if selected date matches increment the total vehicle count by 1
                if row['VehicleType'] == 'Truck': # if the vehicle is a truck increment the total truck count by 1
                    outcomes['total_trucks'] += 1
                if row['elctricHybrid'] == 'True': # if the vehicle is electric and add to the count
                    outcomes["total_electric_vehicles"] += 1
                if row['VehicleType'] in ['Bicycle', 'Motorcycle', 'Scooter']: # check the vehicle if it's a two wheeler and add to the count
                    outcomes["total_two_wheeled"] += 1
                if row['VehicleType'] == 'Bicycle': # check for the bicycle and increment the count by 1
                    outcomes["total_bicycles"] += 1
                
                #check for the busses heading north at the Elm Avenue/ Rabbit road junction and add to the count
                if row['JunctionName'] == 'Elm Avenue/Rabbit Road' and row['travel_Direction_out'] == 'N' and row['VehicleType'] == 'Buss':
                    outcomes["total_busses_north"] += 1
                #check for the vehicles that passes both junctions without turning and increment the count by 1
                if row['travel_Direction_in'] == row['travel_Direction_out']:
                    outcomes["total_no_turn"] += 1
                # if speed limit is over the junction speed limit count the number of vehicles
                if int(row['VehicleSpeed']) > int(row['JunctionSpeedLimit']):
                    outcomes["total_over_speed_limit"] += 1
                #check for the scooter at the Elm Avenue/ Rabbit road junction and add to the count
                if row['JunctionName'] == 'Elm Avenue/Rabbit Road':
                    outcomes["total_elm_avenue"] += 1
                    if row['VehicleType'] == 'Scooter':
                        outcomes['total_scooters_elm_avenue'] += 1
                # check vehicles at Hanley highway/west junction in the peak hour and add to the count
                if row['JunctionName'] == 'Hanley Highway/Westway':                                          
                    outcomes["total_hanley_highway"] += 1
                    hour = int(row['timeOfDay'].split(':')[0])
                    outcomes["hourly_vehicles_hanley_highway"][hour] += 1
                if 'Rain' in row['Weather_Conditions']: # check for the hours of rain and increment the count by 1
                    outcomes["total_rain_hours"] += 1

    except FileNotFoundError: # if a file is not found handles the error file not found
        print(f"File {file_path} not found") 
        return None

    #Calculate the average numbers and percentages

    #calculate the percentage of trucks and round it to the nearest whole number
    outcomes["percentage_trucks"] = round((outcomes['total_trucks'] / outcomes['total_vehicles']) * 100) if outcomes["total_vehicles"] > 0 else 0
    # calculate the average number of bicycles per hour and round it to the nearest whole number 
    outcomes["average_bicycles_per_hour"] = (
        round(outcomes['total_bicycles'] / 24)
        if outcomes['total_two_wheeled'] > 0 
        else 0
    )
    # calculate the percentage of scooters at the elm/Avenue junction and round it to the nearest whole number
    outcomes["percentage_scooters_elm_avenue"] = round((outcomes['total_scooters_elm_avenue'] /outcomes['total_elm_avenue']) * 100 ) if outcomes['total_elm_avenue'] > 0 else 0

    #find the peak hour at hanley hihgway/westway junction
    peak_hour_vehicles = max(outcomes['hourly_vehicles_hanley_highway'])
    outcomes["peak_hours"] = [f"Between {hour:02d} : 00 and {hour+1:02d} : 00" for hour, count in enumerate(outcomes["hourly_vehicles_hanley_highway"]) if count == peak_hour_vehicles]


    return outcomes # return the outcomes dictionary

    pass  # Logic for processing data goes here




def display_outcomes(outcomes): # takes one parameter as outcomes
    """
    Displays the calculated outcomes in a clear and formatted way.
    """
    if outcomes is None: # if no data was found to displat print no data was found to display
        print("No data was found to display")
        return # returns nothing
    
    #print the outcomes in a formatted way 
    print(f"Total number of vehicles : {outcomes['total_vehicles']}")
    print(f"Total number of trucks : {outcomes['total_trucks']}")
    print(f"Total number of electric vehicles : {outcomes['total_electric_vehicles']}")
    print(f"Total number of two wheeled vehicles : {outcomes['total_two_wheeled']}")
    print(f"Total number of busses leaving Elm Avenue/Rabbit Road junction heading north : {outcomes['total_busses_north']}")
    print(f"Total number of vehicles passing through both junctions without turning: {outcomes['total_no_turn']}")
    print(f"Percentage of trucks: {outcomes['percentage_trucks']}%")
    print(f"Average number of bicycles per hour: {outcomes['average_bicycles_per_hour']}")
    print(f"Total number of vehicles over the speed limit: {outcomes['total_over_speed_limit']}")
    print(f"Total number of vehicles at Elm Avenue/Rabbit Road: {outcomes['total_elm_avenue']}")
    print(f"Total number of vehicles at Hanley Highway/Westway: {outcomes['total_hanley_highway']}")
    print(f"Percentage of scooters at Elm Avenue/Rabbit Road: {outcomes['percentage_scooters_elm_avenue']}%")
    print(f"Number of vehicles in the peak hour at Hanley Highway/Westway: {max(outcomes['hourly_vehicles_hanley_highway'])}")
    print(f"Peak traffic hours at Hanley Highway/Westway: {', '.join(outcomes['peak_hours'])}")
    print(f"Total number of hours of rain: {outcomes['total_rain_hours']}")


    pass  # Logic for processing data goes here


# Task C: Save Results to Text File
def save_results_to_file(outcomes, file_name="results.txt"):
    """
    Saves the processed outcomes to a text file and appends if the program loops.
    """

    if outcomes is None: # check if the outcomes is empty and displays the message
        print("No data to display")
        return # returns nothing
    

    try: # try block to handle any errors that may occur
        # open the file in append mode and write the outputs to the file
        with open(file_name, mode = 'a') as file: 
            file.write("Results of the Survey\n")
            file.write(f"Total number of vehicles: {outcomes['total_vehicles']}\n")
            print(f"Total number of vehicles : {outcomes['total_vehicles']}")
            file.write(f"Total number of trucks : {outcomes['total_trucks']}")
            file.write(f"Total number of electric vehicles : {outcomes['total_electric_vehicles']}")
            file.write(f"Total number of two wheeled vehicles : {outcomes['total_two_wheeled']}")
            file.write(f"Total number of busses leaving Elm Avenue/Rabbit Road junction heading north : {outcomes['total_busses_north']}")
            file.write(f"Total number of vehicles passing through both junctions without turning: {outcomes['total_no_turn']}")
            file.write(f"Percentage of trucks: {outcomes['percentage_trucks']}%")
            file.write(f"Average number of bicycles per hour: {outcomes['average_bicycles_per_hour']}")
            file.write(f"Total number of vehicles over the speed limit: {outcomes['total_over_speed_limit']}")
            file.write(f"Total number of vehicles at Elm Avenue/Rabbit Road: {outcomes['total_elm_avenue']}")
            file.write(f"Total number of vehicles at Hanley Highway/Westway: {outcomes['total_hanley_highway']}")
            file.write(f"Percentage of scooters at Elm Avenue/Rabbit Road: {outcomes['percentage_scooters_elm_avenue']}%")
            file.write(f"Number of vehicles in the peak hour at Hanley Highway/Westway: {max(outcomes['hourly_vehicles_hanley_highway'])}")
            file.write(f"Peak traffic hours at Hanley Highway/Westway: {', '.join(outcomes['peak_hours'])}")
            file.write(f"Total number of hours of rain: {outcomes['total_rain_hours']}")

            file.write("-" * 10 + "\n")
        
        print(f"Results saved to {file_name}.") # prints the message that results have been saved to the file
    except Exception as error: # handles any errrors that may occur  and prints the error message
        print(f"An error occured while saving the results : {error}")



    pass  # File writing logic goes here

# if you have been contracted to do this assignment please do not remove this line


if __name__ == "__main__":
    while True:
        date = validate_date_input()
        print(f"Date entered : {date[0]:02d}/{date[1]:02d}/{date[2]:02d}") # prints the date in DD/MM/YYYY format
        if not validate_continue_input(): 
            break 


