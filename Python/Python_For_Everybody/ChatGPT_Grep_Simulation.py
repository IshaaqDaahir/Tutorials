import re

def grep_simulation():
    # Get user input for regular expression
    pattern = input("Enter a regular expression: ")

    # Initialize line counter
    line_count = 0

    try:
        hand = open('mbox.txt')
        for line in hand:
            line = line.rstrip()
            if re.search(pattern, line):
                line_count += 1

        print(f"Number of lines matching the regular expression '{pattern}': {line_count}")

    except FileNotFoundError:
        print("Error: File not found.")

if __name__ == "__main__":
    grep_simulation()
