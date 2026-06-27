def main():

    # Prompt user for text input
    ans = input()

    # Call convert() with user's inputted text and print result to screen
    print(convert(ans))

# Function to convert user's answer from original text to text with emojis
def convert(original):
    return original.replace(":)", "🙂").replace(":(", "🙁")

main()