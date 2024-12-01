import csv
from collections import defaultdict

# Get the date input from user
day = input("Please enter the day of the survey in the format dd: ")
if not day.isdigit():
    print("Integer required")
    exit()
day = int(day)
if day > 31 or day < 1:
    print("Out of range, 01-31 for day")
    exit()

month = input("Please enter the month of the survey in the format MM: ")
if not month.isdigit():
    print("Integer required")
    exit()
month = int(month)
if month > 12 or month < 1:
    print("Out of range, values must be in the range 1 to 12")
    exit()

year = input("Please enter the year of the survey in the format YYYY: ")
if not year.isdigit():
    print("Integer required")
    exit()
year = int(year)

# Construct the date string
selected_date = f"{day:02d}/{month:02d}/{year}"

# List of filenames
filenames = ["traffic_data15062024.csv", "traffic_data21062024.csv", "traffic_data16062024.csv"]

# Initialize variables
total_vehicles = 0
total_trucks = 0
total_electric_vehicles = 0
total_two_wheeled = 0
total_busses_north = 0
total_no_turn = 0
total_over_speed_limit = 0
total_elm_avenue = 0
total_hanley_highway = 0
total_scooters_elm_avenue = 0
hourly_vehicles_hanley_highway = [0] * 24
total_rain_hours = 0

# Read the CSV files
for filename in filenames:
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Date'] != selected_date:
                    continue
                total_vehicles += 1
                if row['VehicleType'] == 'Truck':
                    total_trucks += 1
                if row['elctricHybrid'] == 'True':
                    total_electric_vehicles += 1
                if row['VehicleType'] in ['Bicycle', 'Motorcycle', 'Scooter']:
                    total_two_wheeled += 1
                if row['JunctionName'] == 'Elm Avenue/Rabbit Road' and row['travel_Direction_out'] == 'N' and row['VehicleType'] == 'Buss':
                    total_busses_north += 1
                if row['travel_Direction_in'] == row['travel_Direction_out']:
                    total_no_turn += 1
                if int(row['VehicleSpeed']) > int(row['JunctionSpeedLimit']):
                    total_over_speed_limit += 1
                if row['JunctionName'] == 'Elm Avenue/Rabbit Road':
                    total_elm_avenue += 1
                    if row['VehicleType'] == 'Scooter':
                        total_scooters_elm_avenue += 1
                if row['JunctionName'] == 'Hanley Highway/Westway':
                    total_hanley_highway += 1
                    hour = int(row['timeOfDay'].split(':')[0])
                    hourly_vehicles_hanley_highway[hour] += 1
                if 'Rain' in row['Weather_Conditions']:
                    total_rain_hours += 1
    except FileNotFoundError:
        print(f"File {filename} not found.")
        exit()

# Calculate additional statistics
percentage_trucks = round((total_trucks / total_vehicles) * 100) if total_vehicles > 0 else 0
average_bicycles_per_hour = round(total_two_wheeled / 24)
percentage_scooters_elm_avenue = round((total_scooters_elm_avenue / total_elm_avenue) * 100) if total_elm_avenue > 0 else 0
peak_hour_vehicles = max(hourly_vehicles_hanley_highway)
peak_hours = [f"Between {hour:02d}:00 and {hour+1:02d}:00" for hour, count in enumerate(hourly_vehicles_hanley_highway) if count == peak_hour_vehicles]

# Print the results
print(f"Selected date: {selected_date}")
print(f"Total number of vehicles: {total_vehicles}")
print(f"Total number of trucks: {total_trucks}")
print(f"Total number of electric vehicles: {total_electric_vehicles}")
print(f"Total number of two-wheeled vehicles: {total_two_wheeled}")
print(f"Total number of busses heading north at Elm Avenue/Rabbit Road: {total_busses_north}")
print(f"Total number of vehicles passing through both junctions without turning: {total_no_turn}")
print(f"Percentage of trucks: {percentage_trucks}%")
print(f"Average number of bicycles per hour: {average_bicycles_per_hour}")
print(f"Total number of vehicles over the speed limit: {total_over_speed_limit}")
print(f"Total number of vehicles at Elm Avenue/Rabbit Road: {total_elm_avenue}")
print(f"Total number of vehicles at Hanley Highway/Westway: {total_hanley_highway}")
print(f"Percentage of scooters at Elm Avenue/Rabbit Road: {percentage_scooters_elm_avenue}%")
print(f"Number of vehicles in the peak hour at Hanley Highway/Westway: {peak_hour_vehicles}")
print(f"Peak traffic hours at Hanley Highway/Westway: {', '.join(peak_hours)}")
print(f"Total number of hours of rain: {total_rain_hours}")