# Task C: Save Results to Text File
def save_results_to_file(outcomes, file_name="results.txt"): # take two parameters outcomes and file name with a default value of results.txt
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