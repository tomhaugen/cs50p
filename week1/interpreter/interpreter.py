# CS50P - Week 1 Problem set
# Program that calculates user-typed math equations.

def main():

    # Prompt user to input a math expression and strip whitespace.
    ans = input("Expression: ").strip()
    # Split math expression by spaces as outlined in assumptions of problem statement.
    expression(*ans.split(" "))
    

def expression(x: str, y: str, z: str):
    """Calculates a simple math expression and prints results."""

    # Format inputs for numerical computation.
    x, z = float(x), float(z)

    # Match math expression to User's inputted operator (y) and print results to one decimal place.
    if y == "+":
        print(f"{x + z:.1f}")
    elif y == "-":
        print(f"{x - z:.1f}")
    elif y == "*":
        print(f"{x * z:.1f}")
    elif y == "/":
        print(f"{x / z:.1f}")


if __name__ == "__main__":
    main()