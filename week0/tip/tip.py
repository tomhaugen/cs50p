def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # MY ADDED CODE
    # Use replace() to strip $ from input, then convert string to float. Return result.
    return(float(d.replace("$", "")))



def percent_to_float(p):
    # MY ADDED CODE
    # Use replace() to strip % character from input, then convert string to float, then divide by 100. Return result.
    return(float(p.replace("%", ""))/100)


main()