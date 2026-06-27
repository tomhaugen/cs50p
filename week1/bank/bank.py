def main():
    
    # Prompt the user to enter in a greeting
    ans = input("Greeting: ")

    # Call greeting() with user input after stripping whitespace and converting to lowercase. 
    # Prints greeting() return str.
    print(greeting(ans.strip().lower()))

# Function to evaluate amount of money owed if greeting does not meet requirements
# Returns str answer
def greeting(text):

    # Problem statement outlines that hello gets $0, greetings that start with 'h' get $20, and anything else gets $100
    if text.startswith("hello"):
        return "$0"
    elif text.startswith("h"):
        return "$20"
    else:
        return "$100"

main()