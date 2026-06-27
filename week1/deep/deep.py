def main():
    
    # Ask user to input answer to question of the universe from Hitchhiker's Guide
    ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")

    # Test for acceptable answers as outlined in problem documentation 
    # Print yes on success, print no on fail
    if ans == "42" or ans.lower() == "forty two" or ans.lower() == "forty-two":
        print("Yes")
    else:
        print("No")

main()