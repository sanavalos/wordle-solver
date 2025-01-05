from word_bank import WORD_BANK

def filter_words(correct_letters, incorrect_letters, misplaced_letters):
    filtered = []
    for word in WORD_BANK:
        is_valid = True
        for pos, letter in correct_letters.items():
            if word[pos] != letter:
                is_valid = False
                break
        if any(letter in word for letter in incorrect_letters):
            is_valid = False
        for letter, excluded_pos in misplaced_letters.items():
            if letter not in word or word[excluded_pos] == letter:
                is_valid = False
                break
        if is_valid:
            filtered.append(word)
    return filtered

def get_correct_letters():
    correct = {}
    while True:
        print("\nEnter the correct letter and its position (1-5). Leave blank to stop.")
        letter = input("Letter: ").strip().lower()
        if not letter:
            break
        try:
            position = int(input("Position (1-5): ").strip())
            if 1 <= position <= 5:
                correct[position - 1] = letter
            else:
                print("Position must be between 1 and 5.")
        except ValueError:
            print("Invalid position. Please enter a number.")
    return correct

def get_incorrect_letters():
    incorrect = set(input("\nEnter incorrect letters (e.g., 'abc'): ").strip().lower())
    return incorrect

def get_misplaced_letters():
    misplaced = {}
    while True:
        print("\nEnter a misplaced letter and its position to exclude (1-5). Leave blank to stop.")
        letter = input("Letter: ").strip().lower()
        if not letter:
            break
        try:
            position = int(input("Excluded Position (1-5): ").strip())
            if 1 <= position <= 5:
                misplaced[letter] = position - 1
            else:
                print("Position must be between 1 and 5.")
        except ValueError:
            print("Invalid position. Please enter a number.")
    return misplaced

def main():
    print("Wordle Solver CLI")
    print("===================")
    while True:
        print("\nOptions:")
        print("1. Solve Wordle")
        print("0. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            correct_letters = get_correct_letters()
            incorrect_letters = get_incorrect_letters()
            misplaced_letters = get_misplaced_letters()
            possible_words = filter_words(correct_letters, incorrect_letters, misplaced_letters)
            print("\nPossible Words:")
            print(", ".join(possible_words) if possible_words else "No matches found.")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
