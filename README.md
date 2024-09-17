# Bookbot

**Bookbot** is a command-line tool designed for text analysis. This project focuses on efficiently counting words and providing detailed character frequency analysis from any given `.txt` document. It processes all alphabetic characters, transforming them to lowercase, and disregards non-alphabetic symbols. Additionally, Bookbot provides the total execution time, making it a useful tool for performance analysis on large texts.

## Features
- **Word Count**: Bookbot counts the total number of words in the provided text file.
- **Character Frequency**: It calculates the frequency of each alphabetic character (case-insensitive) and sorts them in descending order by occurrence.
- **Performance Measurement**: The time taken to process the document is displayed at the end of the report.

## How It Works
1. Bookbot reads the content of a text file.
2. It splits the text into individual words and counts them.
3. The program then iterates over the characters, converts them to lowercase, and counts the frequency of each letter (ignoring non-letter characters).
4. The results are sorted by frequency and output in a readable format.
5. Finally, the execution time is displayed to give insight into the processing performance.

## Usage
1. Place your `.txt` file in the appropriate directory.
2. Update the file path in the `book_path` variable in the `main()` function.
3. Run the script, and Bookbot will generate a report with word count, character frequencies, and processing time.

## Example Output
--- Begin report of books/frankenstein.txt --- 
78256 words found in the document

The 'e' character was found 7365 times 
The 't' character was found 5602 times 
The 'a' character was found 5123 times 
... 
--- End report --- 
Time it took to process: 0.345 seconds

## Requirements
- Python 3.x
- A `.txt` file for analysis