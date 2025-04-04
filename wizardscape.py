import random

def generate_grid(rows, cols):
    return [["." for _ in range(cols)] for _ in range(rows)]

def get_random_six_letter_word(file_path):
    with open(file_path, 'r') as f:
        words = [line.strip() for line in f if len(line.strip()) == 6]
    return random.choice(words).upper()



def get_words_from_letters_no_counter(file_path, letters):
    def count_letters(word):
        """Helper function to count letters in a word."""
        letter_counts = {}
        for char in word:
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
        return letter_counts

    # Count the letters in the given word
    letter_counts = count_letters(letters.lower())

    # Read words from the file and filter valid ones
    with open(file_path, 'r') as f:
        words = [line.strip().lower() for line in f]
    valid_words = []
    for word in words:
        word_counts = count_letters(word)
        if all(word_counts.get(char, 0) <= letter_counts.get(char, 0) for char in word_counts):
            valid_words.append(word)
    return valid_words

def gen_extrawords(file_path):






















# Generate a 15x25 grid
grid = generate_grid(15, 25)

# Get a random six-letter word from the file
word = get_random_six_letter_word("corncob-lowercase.txt")

print(sorted(get_words_from_letters_no_counter("corncob-lowercase.txt", word))) #list of word that consist  
print(word)
# Place the six-letter word diagonal xly in the middle of the grid
start_row = (15 - 6) // 2  # Center the word vertically
start_col = (25 - 6) // 2  # Center the word horizontally

for i in range(6):
    grid[start_row + i][start_col + i] = word[i]

# Print the grid with spaces between letters
for row in grid:
    print(" ".join(row))
