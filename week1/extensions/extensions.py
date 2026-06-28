# CS50P - Week 1 Problem set
# Program that takes a user-typed file name and prints the file's media type.

def main():
    
    # Ask the user for a file name.
    ans = input("File name: ")

    # Call media_type() with user input after stripping whitespace and converting to lowercase.
    media_type(ans.strip().lower())


def media_type(filename):
    """Matches the extension of a filename with a media-type."""
    
    # Isolate the extension portion of the user's filename using find().
    at_index = filename.find(".")
    extension = filename[at_index:]

    # Match the filename extension with the problem statement's list of suffixes to check. 
    match extension:
        case ".gif":
            print("image/gif")
        case ".jpg" | ".jpeg":
            print("image/jpeg")
        case ".png":
            print("image/png")
        case ".txt":
            print("text/plain")
        case ".pdf":
            print("application/pdf")
        case ".zip":
            print("application/zip")
        case _:
            print("application/octet-stream")


main()