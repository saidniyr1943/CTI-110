#=============================================================================
# PROGRAM PURPOSE:
# This file is a study guide for file reading, file writing, counting,
# lists, integers, exception handling, and English-to-Morse examples.
# Each section is separate and labeled so you can copy the exact pattern
# you need for a test or lab.
#=============================================================================


#=============================================================================
# 1. BASIC FILE OPEN, READ, WRITE, AND CLOSE
#=============================================================================
# PROGRAM PURPOSE:
# This program shows how to open a file, read from it, write to another file,
# and close the files properly.

def basic_open_read_write_close():
    """Opens files, reads text, writes text, and closes the files."""

    infile = open("input.txt", "r")
    contents = infile.read()
    infile.close()

    outfile = open("output.txt", "w")
    outfile.write(contents)
    outfile.close()


#=============================================================================
# 2. READ A FILE LINE BY LINE
#=============================================================================
# PROGRAM PURPOSE:
# This program opens a file, reads each line one at a time, prints each line,
# and then closes the file.

def read_file_line_by_line(filename):
    """Reads and prints each line from a file."""

    infile = open(filename, "r")

    for line in infile:
        line = line.strip()
        print(line)

    infile.close()


#=============================================================================
# 3. READ INTEGERS FROM A FILE AND ADD THEM
#=============================================================================
# PROGRAM PURPOSE:
# This program reads integers from a file, adds them together, and returns
# the total.

def read_integers_and_sum(filename):
    """Reads integers from a file and returns their sum."""

    infile = open(filename, "r")

    total = 0

    for line in infile:
        number = int(line.strip())
        total += number

    infile.close()

    return total


#=============================================================================
# 4. READ INTEGERS FROM A FILE AND WRITE THE SUM TO ANOTHER FILE
#=============================================================================
# PROGRAM PURPOSE:
# This program reads integers from one file, adds them, then writes the answer
# into another file.

def read_integers_write_sum(input_filename, output_filename):
    """Reads integers, calculates their sum, and writes the sum to a file."""

    infile = open(input_filename, "r")

    total = 0

    for line in infile:
        number = int(line.strip())
        total += number

    infile.close()

    outfile = open(output_filename, "w")
    outfile.write(str(total))
    outfile.close()


#=============================================================================
# 5. COUNT CHARACTERS IN A STRING
#=============================================================================
# PROGRAM PURPOSE:
# This program counts how many times a specific character appears in a string.

def countCharacterInString(text, char):
    """Counts how many times char appears in text."""

    count = 0

    for letter in text:
        if letter == char:
            count += 1

    return count


#=============================================================================
# 6. COUNT CHARACTERS IN A LIST OF WORDS
#=============================================================================
# PROGRAM PURPOSE:
# This program counts how many times a specific character appears in a list
# of strings.

def countCharacterInList(words, char):
    """Counts how many times char appears in a list of words."""

    count = 0

    for word in words:
        for letter in word:
            if letter.lower() == char.lower():
                count += 1

    return count


#=============================================================================
# 7. COUNT CHARACTERS FROM A FILE WITH EXCEPTION HANDLING
#=============================================================================
# PROGRAM PURPOSE:
# This program opens a file, reads all the text, counts how many times a
# character appears, and returns the count. If the file is not found, it
# returns None.

def countCharacterInFile(filename, char):
    """Counts how many times char appears in a file or returns None if missing."""

    try:
        infile = open(filename, "r")
    except FileNotFoundError:
        return None

    count = 0

    for line in infile:
        line = line.strip()

        for letter in line:
            if letter == char:
                count += 1

    infile.close()

    return count


#=============================================================================
# 8. WRITE A LIST INTO A FILE IN A COLUMN
#=============================================================================
# PROGRAM PURPOSE:
# This program writes every item from a list into a file, one item per line.

def writeListColumn(filename, items):
    """Writes each list item on a separate line."""

    outfile = open(filename, "w")

    for item in items:
        outfile.write(str(item) + "\n")

    outfile.close()


#=============================================================================
# 9. WRITE A LIST INTO A FILE SEPARATED BY COMMAS
#=============================================================================
# PROGRAM PURPOSE:
# This program writes a list into a file on one line, separated by commas.

def writeListComma(filename, items):
    """Writes list items on one line separated by commas."""

    outfile = open(filename, "w")

    for i in range(len(items)):
        outfile.write(str(items[i]))

        if i != len(items) - 1:
            outfile.write(", ")

    outfile.close()


#=============================================================================
# 10. WRITE A LIST INTO A FILE NUMBERED
#=============================================================================
# PROGRAM PURPOSE:
# This program writes a list into a file with numbers in front of each item.

def writeListNumbered(filename, items):
    """Writes list items as a numbered list."""

    outfile = open(filename, "w")

    number = 1

    for item in items:
        outfile.write(str(number) + ". " + str(item) + "\n")
        number += 1

    outfile.close()


#=============================================================================
# 11. READ INTEGERS AND WRITE THEM IN A COLUMN
#=============================================================================
# PROGRAM PURPOSE:
# This program reads integers from one file and writes those same integers
# into another file in a column.

def readIntsWriteColumn(input_filename, output_filename):
    """Reads integers and writes them one per line."""

    infile = open(input_filename, "r")
    outfile = open(output_filename, "w")

    for line in infile:
        number = int(line.strip())
        outfile.write(str(number) + "\n")

    infile.close()
    outfile.close()


#=============================================================================
# 12. READ INTEGERS AND WRITE THEM SEPARATED BY COMMAS
#=============================================================================
# PROGRAM PURPOSE:
# This program reads integers from a file and writes them into another file
# on one line separated by commas.

def readIntsWriteComma(input_filename, output_filename):
    """Reads integers and writes them separated by commas."""

    infile = open(input_filename, "r")

    numbers = []

    for line in infile:
        number = int(line.strip())
        numbers.append(number)

    infile.close()

    outfile = open(output_filename, "w")

    for i in range(len(numbers)):
        outfile.write(str(numbers[i]))

        if i != len(numbers) - 1:
            outfile.write(", ")

    outfile.close()


#=============================================================================
# 13. READ INTEGERS AND WRITE THEM NUMBERED
#=============================================================================
# PROGRAM PURPOSE:
# This program reads integers from a file and writes them into another file
# as a numbered list.

def readIntsWriteNumbered(input_filename, output_filename):
    """Reads integers and writes them as a numbered list."""

    infile = open(input_filename, "r")
    outfile = open(output_filename, "w")

    number = 1

    for line in infile:
        value = int(line.strip())
        outfile.write(str(number) + ". " + str(value) + "\n")
        number += 1

    infile.close()
    outfile.close()


#=============================================================================
# 14. READ INTEGERS AND WRITE MIN, MAX, SUM, AND COUNT
#=============================================================================
# PROGRAM PURPOSE:
# This program reads integers from a file, finds the minimum, maximum, sum,
# and count, then writes those answers into another file.

def readIntsWriteStats(input_filename, output_filename):
    """Reads integers and writes min, max, sum, and count to a file."""

    infile = open(input_filename, "r")

    numbers = []

    for line in infile:
        numbers.append(int(line.strip()))

    infile.close()

    total = 0
    count = 0

    for number in numbers:
        total += number
        count += 1

    smallest = numbers[0]
    largest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

        if number > largest:
            largest = number

    outfile = open(output_filename, "w")

    outfile.write("Minimum: " + str(smallest) + "\n")
    outfile.write("Maximum: " + str(largest) + "\n")
    outfile.write("Sum: " + str(total) + "\n")
    outfile.write("Count: " + str(count) + "\n")

    outfile.close()


#=============================================================================
# 15. READ WORDS AND WRITE CHARACTER COUNTS IN A COLUMN
#=============================================================================
# PROGRAM PURPOSE:
# This program takes a list of words, counts how many times a character appears
# in each word, and writes each word with its count into a file.

def writeCharacterCounts(filename, words, char):
    """Writes each word and the count of char in that word."""

    outfile = open(filename, "w")

    for word in words:
        count = 0

        for letter in word:
            if letter.lower() == char.lower():
                count += 1

        outfile.write(word + " " + str(count) + "\n")

    outfile.close()


#=============================================================================
# 16. READ WORDS AND WRITE CHARACTER COUNTS NUMBERED
#=============================================================================
# PROGRAM PURPOSE:
# This program counts a specific character in each word and writes the result
# as a numbered list.

def writeCharacterCountsNumbered(filename, words, char):
    """Writes numbered character counts for each word."""

    outfile = open(filename, "w")

    number = 1

    for word in words:
        count = 0

        for letter in word:
            if letter.lower() == char.lower():
                count += 1

        outfile.write(str(number) + ". " + word + ", " + str(count) + "\n")
        number += 1

    outfile.close()


#=============================================================================
# 17. READ WORDS FROM A FILE AND WRITE THEM NUMBERED
#=============================================================================
# PROGRAM PURPOSE:
# This program reads words from an input file and writes them into another file
# as a numbered list.

def readWordsWriteNumbered(input_filename, output_filename):
    """Reads words from a file and writes them numbered."""

    infile = open(input_filename, "r")
    outfile = open(output_filename, "w")

    number = 1

    for line in infile:
        word = line.strip()
        outfile.write(str(number) + ". " + word + "\n")
        number += 1

    infile.close()
    outfile.close()


#=============================================================================
# 18. READ WORDS FROM A FILE AND WRITE THEM SEPARATED BY COMMAS
#=============================================================================
# PROGRAM PURPOSE:
# This program reads words from a file and writes them into another file on
# one line separated by commas.

def readWordsWriteComma(input_filename, output_filename):
    """Reads words and writes them separated by commas."""

    infile = open(input_filename, "r")

    words = []

    for line in infile:
        words.append(line.strip())

    infile.close()

    outfile = open(output_filename, "w")

    for i in range(len(words)):
        outfile.write(words[i])

        if i != len(words) - 1:
            outfile.write(", ")

    outfile.close()


#=============================================================================
# 19. SAFE FILE READING WITH EXCEPTION HANDLING
#=============================================================================
# PROGRAM PURPOSE:
# This program safely opens and reads a file using exception handling.
# If the file is not found, it returns None.

def safeReadFile(filename):
    """Reads a file safely or returns None if the file is not found."""

    try:
        infile = open(filename, "r")
    except FileNotFoundError:
        return None

    contents = infile.read()
    infile.close()

    return contents


#=============================================================================
# 20. INTEGER-SUM FILE PROBLEM WITH EXCEPTION HANDLING
#=============================================================================
# PROGRAM PURPOSE:
# This program reads integers from a file and returns their sum. If the file
# does not exist, it returns None.

def safeReadSum(filename):
    """Reads integers from a file and returns their sum or None if file not found."""

    try:
        infile = open(filename, "r")
    except FileNotFoundError:
        return None

    total = 0

    for line in infile:
        total += int(line.strip())

    infile.close()

    return total


#=============================================================================
# 21. ENGLISH TO MORSE, THEN WRITE IN A COLUMN
#=============================================================================
# PROGRAM PURPOSE:
# This program translates English words into Morse code and writes each word
# and Morse translation in a column.

def buildMorseDictionary():
    """Creates and returns an English-to-Morse dictionary."""

    return {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
        "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
        "Z": "--.."
    }


def translateWordToMorse(word):
    """Translates one English word into Morse code."""

    morse = buildMorseDictionary()
    result = ""

    for ch in word.upper():
        if ch in morse:
            result += morse[ch] + " "

    return result.strip()


def writeMorseColumn(filename, words):
    """Writes each word and its Morse translation in a column."""

    outfile = open(filename, "w")

    for word in words:
        morse_word = translateWordToMorse(word)
        outfile.write(word + " " + morse_word + "\n")

    outfile.close()


#=============================================================================
# 22. ENGLISH TO MORSE, THEN WRITE NUMBERED
#=============================================================================
# PROGRAM PURPOSE:
# This program translates English words into Morse code and writes them as a
# numbered list.

def writeMorseNumbered(filename, words):
    """Writes Morse translations as a numbered list."""

    outfile = open(filename, "w")

    number = 1

    for word in words:
        morse_word = translateWordToMorse(word)
        outfile.write(str(number) + ". " + word + ", " + morse_word + "\n")
        number += 1

    outfile.close()


#=============================================================================
# QUICK MEMORY PATTERNS
#=============================================================================

# Open file for reading:
# infile = open(filename, "r")

# Open file for writing:
# outfile = open(filename, "w")

# Read one line:
# line = infile.readline()

# Read all lines one at a time:
# for line in infile:
#     line = line.strip()

# Write one line:
# outfile.write(str(value) + "\n")

# Close files:
# infile.close()
# outfile.close()

# File not found exception handling:
# try:
#     infile = open(filename, "r")
# except FileNotFoundError:
#     return None


#=============================================================================
# SAMPLE MAIN FOR TESTING ONLY
#=============================================================================
# This main function is optional. You can comment it out during testing if your
# teacher only wants functions.

def main():
    """Runs a few small examples from this file."""

    print(countCharacterInString("mississippi", "s"))
    print(countCharacterInList(["Apple", "Banana", "Cherry"], "a"))
    print(translateWordToMorse("hello"))


if __name__ == "__main__":
    main()
