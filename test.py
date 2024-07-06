import sys

# Get the word from the user
word_to_count = input("Enter the word: ")

# Read input from user until EOF
input_text = sys.stdin.read()

# Count the occurrences of the word in the input
count = input_text.count(word_to_count)

# Print the count
print(count, word_to_count)

