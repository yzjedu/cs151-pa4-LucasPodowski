

# Purpose: Display the menu selections to user
# Parameters: none
# Return: none
def display_menu():
    print("\nOptions:")
    print("1. Count headlines with a specific word")
    print("2. Write headlines containing a specific word to a new file")
    print("3. Determine the average number of characters per headline")
    print("4. Output the longest and shortest headlines")
    print("5. Load a new file")
    print("6. Quit")

# Purpose: Load and read the file into a list
# Parameters: filename
# Return: headlines or 0 to continue the loop
def load_file(file_name):
    try:
        headlines = []
        with open(file_name, 'r') as file:
            for line in file:
               headlines.append(line.strip())
        print(f"Successfully loaded {len(headlines)} headlines from '{file_name}'.")
        return headlines
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found. Please try again.")
        return 0

# Purpose: count and output the number of headlines containing a word
# Parameters: headlines and word
# Return: none
def count_headlines_with_word(headlines, word):
    count = 0
    search_word = f' {word.lower().strip()} '
    for headline in headlines:
        if search_word in headline:
            count += 1
    print(f"Number of headlines containing '{word}': {count}")

# Purpose: Write the headlines containing a word into another file with a name chosen by the user
# Parameters: headlines, word, and the output_file
# Return: none
def write_headlines_with_word(headlines, word, output_file):
    search_word = f' {word.lower().strip()} '
    matches = []
    for headline in headlines:
        if search_word in headline.lower():
            matches.append(headline)
    with open(output_file, 'w') as file:
        for headline in matches:
            file.write(headline + "\n")
    print(f"Saved {len(matches)} headlines containing '{word}' to '{output_file}'.")

# Purpose: Calculates and outputs the average length of the element contained in a list
# Parameters: headlines
# Return: none
def calculate_average_length(headlines):
    total_length = 0
    for headline in headlines:
        total_length += len(headline)
    avg_length = total_length / len(headlines)
    print(f"The average number of characters per headline is: {avg_length:.2f}")

# Purpose: find and output the shortest and longest elements in a list
# Parameters: headlines
# Return: none
def find_longest_and_shortest_headlines(headlines):
    longest = max(headlines, key=len) # I found this method on stack overflow: https://stackoverflow.com/questions/873327/pythons-most-efficient-way-to-choose-longest-string-in-list
    shortest = min(headlines, key=len)
    print(f"Longest headline ({len(longest)} characters): {longest}")
    print(f"Shortest headline ({len(shortest)} characters): {shortest}")


# Purpose: Be used as a main function with a loop to continue the program and ask the user which analysis they
# want to use on the file they choose
# Parameters: none
# Return: none
def main():
    print("Welcome to the ABC Headline Analyzer!")
    print("This program analyzes headlines from a file you choose.")
    print("You can perform various analyses or switch to a different file at any time.")
    print("-" * 60)

    headlines = []
    continue_program = 'continue'
    SENTINEL = 0
    # Initial file loading
    while SENTINEL == 0:
        file_name = input("Enter the name of the file to analyze: ").strip()
        headlines = load_file(file_name)
        SENTINEL = headlines
        if SENTINEL == 0:
            print("Please provide a valid file to proceed.")

    # Main interaction loop
    while not continue_program == 'end':
        display_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            word = input("Enter a word to search for: ").strip()
            count_headlines_with_word(headlines, word)
        elif choice == "2":
            word = input("Enter a word to search for: ").strip()
            output_file = input("Enter the name of the output file: ").strip()
            write_headlines_with_word(headlines, word, output_file)
        elif choice == "3":
            calculate_average_length(headlines)
        elif choice == "4":
            find_longest_and_shortest_headlines(headlines)
        elif choice == "5":
            file_name = input("Enter the name of the new file to analyze: ").strip()
            headlines = load_file(file_name)
            if not headlines:
                print("The file could not be loaded. Please choose another option.")
        elif choice == "6":
            continue_program = 'end'
            print("Exiting the program. Goodbye!")
        else:
            print("Invalid choice. Please select a whole number between 1 and 6: ")

        if not continue_program =='end':
            print("-" * 60)

main()