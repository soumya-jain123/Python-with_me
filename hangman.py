import random

class Hangman:
    def __init__(self, wordlist_file):
        self.wordlist = self.load_wordlist(wordlist_file)
        self.word_to_guess = self.get_random_word()
        self.displayed_word = ["_"] * len(self.word_to_guess)
        self.guessed_letters = []
        self.num_wrong = 0
        self.num_guesses = 0
        self.max_wrong_guesses = 6

    def load_wordlist(self, filename):
        try:
            with open(filename, "r") as file:
                return [word.strip().upper() for word in file.readlines()]
        except FileNotFoundError:
            print(f"Error: Wordlist file '{filename}' not found.")
            return []

    def get_random_word(self):
        return random.choice(self.wordlist)

    def add_spaces(self, word):
        return " ".join(word)

    def draw_screen(self):
        print("-" * 79)
        print("Word:", self.add_spaces(self.displayed_word),
              " Guesses:", self.num_guesses,
              " Wrong:", self.num_wrong,
              " Tried:", self.add_spaces(self.guessed_letters))
        self.draw_hangman()

    def draw_hangman(self):
        hangman_parts = [
            "  O   ",
            " /|\\  ",
            " / \\  ",
        ]

        for i in range(min(self.num_wrong, len(hangman_parts))):
            print(hangman_parts[i])


    def get_letter(self):
        while True:
            guess = input("Enter a letter: ").strip().upper()

            if guess == "" or len(guess) > 1 or not guess.isalpha():
                print("Invalid entry. Please enter one valid letter.")
                continue

            if guess in self.guessed_letters:
                print("You already tried that letter.")
                continue
            else:
                return guess

    def play(self):
        while "_" in self.displayed_word and self.num_wrong < self.max_wrong_guesses:
            self.draw_screen()

            guess = self.get_letter()

            self.guessed_letters.append(guess)
            self.num_guesses += 1

            if guess in self.word_to_guess:
                for i in range(len(self.word_to_guess)):
                    if self.word_to_guess[i] == guess:
                        self.displayed_word[i] = guess
            else:
                self.num_wrong += 1

        self.draw_screen()

        if "_" not in self.displayed_word:
            print("Congratulations! You guessed the word:", "".join(self.displayed_word))
        else:
            print("Sorry, you ran out of guesses. The word was:", self.word_to_guess)

if __name__ == "__main__":
    wordlist_file = "D:\wordlist.txt"
    game = Hangman(wordlist_file)
    game.play()
