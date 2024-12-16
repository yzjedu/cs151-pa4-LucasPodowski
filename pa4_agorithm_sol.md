# Algorithm for the ABC Headline Analyzer Program

---

### Algorithm for `read_filename`
- **Purpose**: Prompt the user to input a filename and ensure the file exists. 
- **Name**: `read_filename`
- **Parameters**: None
- **Return**: The valid filename entered by the user.
- **Algorithm**:
  1. Prompt the user to input the filename.
  2. While the file does not exist:
      1. Display an error message indicating the file is not found.
      2. Prompt the user to input the filename again.
  3. Return the valid filename.

---

### Algorithm for `read_headlines`
- **Purpose**: Read and store headlines from the provided file.
- **Name**: `read_headlines`
- **Parameters**: `filename` (string) - The name of the file containing headlines.
- **Return**: A list of headlines from the file.
- **Algorithm**:
  1. Initialize an empty list `headlines`.
  2. Open the file in read mode.
    1. For each line in the file:
        1. Strip leading and trailing whitespace from the line.
        2. Add the cleaned line to `headlines`.
  4. Return the list `headlines`.

---

### Algorithm for `count_word_occurrences`
- **Purpose**: Count the number of occurrences of a specific word in the list of headlines.
- **Name**: `count_word_occurrences`
- **Parameters**:
  - `headlines` (list of strings): The list of headlines to search.
  - `word` (string): The word to search for.
- **Return**: The count of occurrences as an integer.
- **Algorithm**:
  1. Initialize a counter `count` to 0.
  2. For each headline in `headlines`:
      1. Convert the headline to lowercase and split it into words.
      2. Count the occurrences of `word` (converted to lowercase) in the headline.
      3. Add the count of occurance to `count`.
  3. Return the total `count`.

---

### Algorithm for `write_headlines_with_word`
- **Purpose**: Write all headlines containing a specific word to a new file.
- **Name**: `write_headlines_with_word`
- **Parameters**:
  - `headlines` (list of strings): The list of headlines to search.
  - `word` (string): The word to search for.
  - `output_file` (string): The name of the output file.
- **Return**: None.
- **Algorithm**:
  1. Open the `output_file` in write mode.
    1. For each headline in `headlines`:
        1. If `word` (converted to lowercase) is in the headline (converted to lowercase):
            1. Write the headline to `output_file`.

---

### Algorithm for `calculate_average_length`
- **Purpose**: Calculate the average length of headlines in characters.
- **Name**: `calculate_average_length`
- **Parameters**: `headlines` (list of strings) - The list of headlines.
- **Return**: The average length as a float.
- **Algorithm**:
  1. Initialize an accumulator `total_characters` to 0.
  2. For each headline in `headlines`:
    1. Get the total number of characters in a headline using the `len` function add it to `total_characters` .
  3. Return the result by dividing `total_characters` by the number of headlines.

---

### Algorithm for `find_longest_headline`
- **Purpose**: Find the longest headline by character count.
- **Name**: `find_longest_headline`
- **Parameters**: `headlines` (list of strings) - The list of headlines.
- **Return**: The longest headline as a string.
- **Algorithm**:
  1. Initialize `longest` as the first headline in `headlines`.
  2. For each headline in `headlines`:
      1. If the length of the headline is greater than the length of `longest`:
          1. Update `longest` to the current headline.
  3. Return `longest`.

---

### Algorithm for `find_shortest_headline`
- **Purpose**: Find the shortest headline by character count.
- **Name**: `find_shortest_headline`
- **Parameters**: `headlines` (list of strings) - The list of headlines.
- **Return**: The shortest headline as a string.
- **Algorithm**:
  1. Initialize `shortest` as the first headline in `headlines`.
  2. For each headline in `headlines`:
      1. If the length of the headline is less than the length of `shortest`:
          1. Update `shortest` to the current headline.
  3. Return `shortest`.

---


### Algorithm for `get_menu_option`
- **Purpose**: Display menu options and get a valid menu option from the user.
- **Name**: `get_menu_option`
- **Parameters**: None
- **Return**: A valid menu option as an integer (1 to 7).
- **Algorithm**:
  1. Display the menu options:
      - 1. Count headlines containing a specific word.
      - 2. Write headlines with a specific word to a new file.
      - 3. Calculate average headline length.
      - 4. Find the longest headlines.
      - 5. Find the shortest headlines.
      - 6. Load a new file.
      - 7. Quit.
  2. Prompt the user to enter a menu choice (1-7).
  3. While the input is invalid (not a digit or not between 1 and 7):
      1. Display an error message.
      2. Prompt the user to enter the choice again.
  4. Convert the valid input to an integer and return it.

---

### Algorithm for `main`
- **Purpose**: Main function to drive the ABC Headline Analyzer program.
- **Name**: `main`
- **Parameters**: None
- **Return**: None
- **Algorithm**:
  1. Display a welcome message and introduce the program.
  2. Initialize an empty list `headlines` to store the file content.
  3. Set the variable `choice` to `'yes'` to control the main loop.
  4. While the user does not choose to quit by selecting `7`:
      1. If `headlines` is empty:
          1. Call `read_filename()` to prompt the user for a filename.
          2. Call `read_headlines(filename)` to read and load the headlines into the `headlines` list.
          3. Display a message indicating the file has been loaded and the number of headlines.
      2. Call `get_menu_option()` to display the menu and get the user's choice.
      3. Process the user’s choice:
       1. If the choice is `'1'`:
         1. Prompt the user to input the word to search for.
         2. Call `count_word_occurrences(headlines, word)` to count occurrences of the word.
         3. Display the count of the word in the headlines.
       1. Otherwise, If the choice is `'2'`:
         1. Prompt the user to input the word to search for.
         2. Prompt the user to input the name of the output file.
         3. Call `write_headlines_with_word(headlines, word, output_file)` to write matching headlines to the file.
         4. Display a success message indicating the headlines have been written.
       1. Otherwise, If the choice is `'3'`:
         1. Call `calculate_average_length(headlines)` to calculate the average length of the headlines.
         2. Display the average headline length with two decimal precision.
       1. Otherwise, If the choice is `'4'`:
         1. Call `find_longest_headline(headlines)` to find the longest headline.
         2. Display the longest headline.
       1. Otherwise, If the choice is `'5'`:
         1. Call `find_shortest_headline(headlines)` to find the shortest headline.
         2. Display the shortest headline.
       1. Otherwise, If the choice is `'6'`:
         1. Reset `headlines` to an empty list.
         2. Display a message indicating the program is ready to load a new file.
         3. Clear the console screen.
       1. Otherwise, If the choice is `'7'`:
         1. Display a goodbye message.
         2. Set `choice` to `'no'` to exit the loop.
       1. Otherwise:
         1. Display an error message for invalid input.
