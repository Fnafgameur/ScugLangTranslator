import time

words = {
    "A": "A",
    "B": "Wawaa",
    "C": "Wa",
    "D": "Aw",
    "E": "Waa",
    "F": "Ww",
    "G": "Waw",
    "H": "Wwa",
    "I": "Wawa",
    "J": "Aaw",
    "K": "Waaw",
    "L": "Waww",
    "M": "Awa",
    "N": "Wwaa",
    "O": "Waawa",
    "P": "Wwaw",
    "Q": "Aa",
    "R": "Awawa",
    "S": "Awaa",
    "T": "Aww",
    "U": "Awwa",
    "V": "Wawwa",
    "W": "W",
    "X": "Wawaa",
    "Y": "Awaww",
    "Z": "Awaw",
    " ": "Wawaw"
}

print("Welcome to Scug Translator!")


def main():

    while True:
        print("")
        print("1. Normal text to Scug text")
        print("2. Scug text to Normal text")
        print("3. Dictionary")
        print("q. Exit")
        choice = (input("Enter your choice: ")
                  .replace(" ", "")
                  .lower())
        choice = choice[0]

        match choice:
            case "1":
                print("")
                normal_to_scug()
            case "2":
                print("")
                scug_to_normal()
            case "q":
                print("")
                print("Exiting...")
                time.sleep(1)
                break
            case "3":
                print("")
                display_dictionary()
                break
            case _:
                print("")
                print("Invalid choice! Please try again.")
                time.sleep(1)
                continue


def normal_to_scug():
    choice = "y"

    while choice != "n":
        text = input("Enter the normal text: ")
        result = ""

        for char in text:

            if char == " ":
                result += "Wawaw "
                continue

            modifiedChar = char.upper()

            if modifiedChar in words:
                result += words[modifiedChar] + " "
            else:
                result = "Unexpected character at position " + str(text.index(char) + 1) + ": " + char

        print("result : " + result)
        choice = (input("Do you want to continue on this mode? (Y/n): ")
                  .replace(" ", "")
                  .lower())
    main()


def scug_to_normal():
    choice = "y"

    while choice != "n":
        text = input("Enter the scug text: ")
        result = ""
        char = 0

        while char < len(text):
            if char == " ":
                continue

            word = ""

            if text[char] != " ":
                while char < len(text) and text[char] != " ":
                    word += text[char]
                    char += 1

                    if char < len(text) and text[char] == " ":
                        char += 1
                        break
            else:
                word = "wawaw"

            word = word[0].upper() + word[1:]

            if word in words.values():
                for key, value in words.items():
                    if value == word:
                        result += key
                        break
            else:
                result = "Unexpected word at position " + str(char) + ": " + word
                break

        print("result : " + result)

        choice = (input("Do you want to continue on this mode? (Y/n): ")
                  .replace(" ", "")
                  .lower())
    main()


def display_dictionary():
    print("Dictionary:")
    for key, value in words.items():
        if key == " ":
            key = "[Space]"
        print(key + " : " + value)
    print("")


if __name__ == '__main__':
    main()
