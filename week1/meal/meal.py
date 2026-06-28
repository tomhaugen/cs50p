# CS50P - Week 1 Problem set
# Program that tells what meal to eat at a given time.

def main():

    # Prompt the user to input time in either ##:## or ##:## a.m/p.m. formats
    ans = input("What time is it? ").strip()
    
    # Call convert() to change user input to numerical format for if/elif tests.
    num_time = convert(ans)
    
    # Check to see if time is between meal times to print appropriate meal.
    # If not within any window, print nothing as required in problem.
    if 7 <= num_time <= 8:
        print("breakfast time")
    elif 12 <=  num_time <= 13:
        print("lunch time")
    elif 18 <= num_time <= 19:
        print("dinner time")     

def convert(time):
    """Converts time in str to numerical."""

    # Check to see if user time input is in 24-hr or 12-hr format.
    # User inputted format potentialities are limited by problem statement.
    if " " in time:
        clock, meridiem = time.split(" ")
    else:
        clock = time
        meridiem = None
    
    # Seperate clock list into hours and minutes then convert to float for numerical time computation.
    hours, minutes = clock.split(":")
    hours = float(hours)
    minutes = float(minutes)

    # Clean up meridiem for conversion from 12-hr time to 24-hr time.
    if meridiem:
        meridiem = meridiem.lower().replace(".", "")

    # Convert 12-hr time into 24-hr time.
    if meridiem == "pm" and hours != 12:
        hours += 12
    elif meridiem == "am" and hours == 12:
        hours = 0

    # Calculate numerical time from 24-hr format.
    return hours + minutes / 60


if __name__ == "__main__":
    main()