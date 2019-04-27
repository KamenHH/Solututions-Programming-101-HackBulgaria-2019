def get_word():
    from sys import argv
    return argv[1]


def print_word(letter_lst):
    for letter in letter_lst:
        print(letter, end=' ')
    print('')


def print_hangedman():
    print("""You lost!
 _________
|    |    |
|  \ O /  |
|    |    |
|    |    |
|   / \   |\n""")


def hangman(word):
    tries = 10
    curr_match = ['_']*len(word)
    letter_list = [ch for ch in word]
    print("Welcome to Hangman! Let's play!\n"+"_ "*len(word))
    while tries:
        if '_' not in curr_match:
            print("Congrats! You guessed the word!")
            return
        letter = input("Guess a letter: ")
        if letter not in letter_list:
            print('Incorrect!')
            tries -= 1
        while letter in letter_list:
            indx = letter_list.index(letter)
            curr_match[indx] = letter
            letter_list.pop(indx)
            letter_list.insert(indx, '_')
        print_word(curr_match)
    print_hangedman()


def main():
    word = get_word()
    hangman(word)


if __name__ == '__main__':
    main()



