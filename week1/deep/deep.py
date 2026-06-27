def main():
    
    # Ask user to input answer to question of the universe from Hitchhiker's Guide
    ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    
    # Take user answer, strip whitespace and make lower case to streamline test cases in question()  
    question(ans.lower().strip())

def question(guess):
    
    # Test for acceptable answers as outlined in problem documentation 
    # Print yes on success, print no on fail
    if guess == "42" or guess == "forty two" or guess == "forty-two":
        print("Yes")
    else:
        print("No")

main()