import os

# Purpose: Read and validate the input filename.
# Parameters: None
# Returns: A valid filename as a string.
def read_filename():
    filename = input("Enter the filename to analyze: ").strip()
    while not os.path.isfile(filename):
        print("File not found. Please try again.")
        filename = input("Enter the filename to analyze: ").strip()
    return filename

# Purpose: Read and store headlines from a file.
# Parameters: filename (string)
# Returns: A list of headlines from the file.
def read_headlines(filename):
    headlines = []
    with open(filename, 'r') as file:
       for line in file:
           line = line.strip()
           headlines.append(line)
    return headlines

# Purpose: Count the occurrences of a specific word in headlines.
# Parameters: headlines (list of strings), word (string)
# Returns: The count of occurrences as an integer.
def count_word_occurrences(headlines, word):
    count = 0
    for headline in headlines:
        count += headline.lower().split().count(word.lower())
    return count

# Purpose: Write headlines containing a specific word to a new file.
# Parameters: headlines (list of strings), word (string), output_file (string)
# Returns: None
def write_headlines_with_word(headlines, word, output_file):
    with open(output_file, 'w') as file:
        for headline in headlines:
            if word.lower() in headline.lower():
                file.write(headline + '\n')

# Purpose: Calculate the average length of headlines in characters.
# Parameters: headlines (list of strings)
# Returns: The average length as a float.
def calculate_average_length(headlines):
    total_characters = sum(len(headline) for headline in headlines)
    return total_characters / len(headlines)

# Purpose: Find the longest headline by character count.
# Parameters: headlines (list of strings)
# Returns: The longest headline as a string.
def find_longest_headline(headlines):
    longest = headlines[0]
    for headline in headlines:
        if len(headline) > len(longest):
            longest = headline
    return longest

# Purpose: Find the shortest headline by character count.
# Parameters: headlines (list of strings)
# Returns: The shortest headline as a string.
def find_shortest_headline(headlines):
    shortest = headlines[0]
    for headline in headlines:
        if len(headline) < len(shortest):
            shortest = headline
    return shortest

# Purpose: Main function to drive the program.
# Parameters: None
# Returns: None
def main():
    print("Welcome to the ABC Headline Analyzer!")
    print("-------------------------------------")

    headlines = []
    choice = 'yes'
    while choice != 'no':
        if not headlines:
            filename = read_filename()
            headlines = read_headlines(filename)
            print(f"File '{filename}' loaded successfully with {len(headlines)} headlines.\n")

        print("Menu Options:")
        print("\t1. Count headlines containing a specific word.")
        print("\t2. Write headlines with a specific word to a new file.")
        print("\t3. Calculate average headline length.")
        print("\t4. Find the longest headlines.")
        print("\t5. Find the shortest headlines.")
        print("\t6. Load a new file.")
        print("\t7. Quit.")

        choice = input("Enter your choice: ").strip()
        if choice == '1':
            word = input("Enter the word to search for: ").strip()
            count = count_word_occurrences(headlines, word)
            print(f"The word '{word}' appears in {count} headlines.\n")
        elif choice == '2':
            word = input("Enter the word to search for: ").strip()
            output_file = input("Enter the name of the output file: ").strip()
            write_headlines_with_word(headlines, word, output_file)
            print(f"Headlines containing '{word}' have been written to '{output_file}'.\n")
        elif choice == '3':
            average_length = calculate_average_length(headlines)
            print(f"The average headline length is {average_length:.2f} characters.\n")
        elif choice == '4':
            longest = find_longest_headline(headlines)
            print(f"The shortest headline is: {shortest}")
        elif choice == '5':
            shortest= find_shortest_headline(headlines)
            print(f"The shortest headline is: {shortest}")
        elif choice == '6':
            headlines = []
            print("Ready to load a new file.\n")
        elif choice == '7':
            print("Thank you for using the ABC Headline Analyzer. Goodbye!")
            choice = 'no'
        else:
            print("Invalid choice. Please try again.\n")

main()