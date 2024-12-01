import csv
from collections import defaultdict

# Task B: Processed Outcomes
def process_csv_data(file_path, selected_date): # takes two parameters as file to the path and the for the date selected
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




def display_outcomes(outcomes):
    """
    Displays the calculated outcomes in a clear and formatted way.
    """
    if outcomes is None:
        print("No data was found to display")
        return
    
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


file_path = 'traffic_data15062024.csv'
selected_date = '15/06/2024'

outcomes = process_csv_data(file_path, selected_date)
display_outcomes(outcomes)