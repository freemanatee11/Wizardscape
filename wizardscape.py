import random
#For grid and all printing purposes#
def interface():
    basis = all_words("corncob-lowercase.txt", 6) #Total available words of length at most 6#
    gamestate = generate_grid(15, 25) #grid to edit/place words onto
    available_main_words = all_words_givlen("corncob-lowercase.txt", 6) #Total available words of length 6#
    main_word = random.choice(available_main_words) #Main Word to guess#
    next_available_words = generate_words(main_word, basis)
    main_checker = [] #For intersecting purposes#
    for i in main_word:
        main_checker.append(i)

    #list of lists of pairs of letters + coordinates, to be used for placing words at the grid    
    main_word_coords = [(n, (i, j)) for i, j, n in zip(list(range(2,13,2)), list(range(7,18,2)), [k for k in main_word.upper()])] 
    
    for i in next_available_words:
        if i == main_word:
            next_available_words.remove(main_word)
    print(main_word.upper(), next_available_words)

    #Pairing letters with coords. Note this is 0-indexing#
    next_words = breakdown(choose_n_words(next_available_words, main_checker))
    split_words = splits(next_words, main_checker)
    print("Place: ", next_words)
    print("Splitted: ", split_words)
    print("Remaining Words: ", next_available_words)

    words_on_grid = place_everything(split_words, main_word_coords, "vertical")

    
    #Putting the words on grid#
    for words in words_on_grid:
        for z, (y, x) in words:
            gamestate[y][x] = z
    for n, (i, j) in main_word_coords:
        gamestate[i][j] = n


    #Printing grid#
    for i in gamestate:
        print(" ".join(i))


    print(main_word_coords)
    return words_on_grid




""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#One directional pairing of words, to be changed#

def place_everything(to_place, intersections, orientation):
    words_to_place = []
    for a, b in zip(to_place, intersections):
        words_to_place.append(place(a, b, orientation))
    return words_to_place


def place(splitted, intersection, orientation):
    less, great = splitted
    inter, (y, x) = intersection
    if orientation == "horizontal":
        paired_up = []
        left = len(less)
        right = len(great)
        for letter, j in zip(less, list(range(x - left, x))):
            paired_up.append((letter, (y, j)))
        for letter, j in zip(great, list(range(x + 1, x + right + 1))):
            paired_up.append((letter, (y, j)))
    else:
        paired_up = []
        up = len(less)
        down = len(great)
        for letter, i in zip(less, list(range(y - up, y))):
            paired_up.append((letter, (i, x)))
        for letter, i in zip(great, list(range(y + 1, y + down + 1))):
            paired_up.append((letter, (i, x)))
    return paired_up

#Splits the next words into 2 parts, one on the "left/up", the other on the "right/down"#
def split_first_instance(word, letter):
    loc = word.index(letter)
    return [word[:loc], word[loc + 1:]]

def splits(words, letters):
    splitted = []
    for word, letter in zip(words, letters):
        splitted.append(split_first_instance(word, letter))
    return splitted    


#Breaks down string into list of letters#

def breakdown(lst):
    separated_words = []
    for word in lst:
        separated_word = []
        for letter in word:
            separated_word.append(letter)
        separated_words.append(separated_word)

    return separated_words
              
#Choose words based on the intersecting letter, ensuring that an intersection exists#
def choose_n_words(choose_here, letters):
    chosen_words = []
    for i in letters:
        viable = [x for x in choose_here if i in x]
        next_word = random.choice(viable)
        chosen_words.append(next_word)
        choose_here.remove(next_word)
    return chosen_words



#All words possible of length at most a number#
def all_words(file_path, length):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if len(line.strip()) <= length]

#Anagrams, used for the next words after main word#
def generate_words(word, dictionary):
    def get_permutations(word, length):
        if length == 1:
            return list(word)
        else:
            result = []
            for i in range(len(word)):
                char = word[i]
                remaining_word = word[:i] + word[i+1:]
                for perm in get_permutations(remaining_word, length - 1):
                    result.append(char + perm)
            return result

    results = set()

    for length in range(3, len(word) + 1):
        perms = get_permutations(word, length)
        for perm in perms:
            if perm in dictionary:
                results.add(perm)

    return sorted(results)

#Shows available words of a given length only#
def all_words_givlen(file_path, length):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if len(line.strip()) == length]
    
#Main grid#
def generate_grid(rows, cols):
    return [["." for _ in range(cols)] for _ in range(rows)]

print(interface())
