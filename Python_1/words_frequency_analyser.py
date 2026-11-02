# from pathlib import Path 

# def file_type_detector():
#     directory = input("Enter directory path: ").strip()
#     folder = Path(directory)

#     try:
#       if not folder.exists():
#         print("Error: Path does not exist.")
#         return None
#       elif not folder.is_file():
#        print("Error: Path is not a file.")
#        return None
#       elif folder.suffix.lower() != ".txt":
#        print("Error: Invalid file type.")
#        return None


#       content = folder.read_text(encoding="utf-8")

#       if not content.strip():
#         print("Error: The file is empty.")
#         return None

#       else:
#         print("File read successfully!")
#         return content        


#     except FileNotFoundError:
#         print("File does not exist.")
#         return None
#     except PermissionError:
#         print("Permission denied.")
#         return None
#     except UnicodeDecodeError:
#         print("Invalid text encoding.")
#         return None
#     except OSError as e:
#         print(f"File error: {e}")

#     return None

   



# def word_freq(text):
#      words = text.split()
#      freq = {}
#     for word in words:
#         word = word.lower()
#         if word.lower()==word.upper():
#             continue
#         elif word in freq:
#             freq[word] += 1
#         else:
#             freq[word] = 1
#     for word, count in freq.items():
#         print(f"{word}: {count}")

#  return freq


# user_input = input("Do you want to analyze another string? (yes/no): ")
# while user_input.lower() == "yes":
#     word_freq()
#     user_input = input("Do you want to analyze another string? (yes/no): ")
#     result = word_freq()




from pathlib import Path


def file_type_detector():
    directory = input("Enter file path: ").strip()
    folder = Path(directory)

    try:
        if not folder.exists():
            print("Error: Path does not exist.")
            return None

        elif not folder.is_file():
            print("Error: Path is not a file.")
            return None

        elif folder.suffix.lower() != ".txt":
            print("Error: Invalid file type.")
            return None

        content = folder.read_text(encoding="utf-8")

        if not content.strip():
            print("Error: The file is empty.")
            return None

        print("File read successfully!")
        return content

    except FileNotFoundError:
        print("File does not exist.")
        return None

    except PermissionError:
        print("Permission denied.")
        return None

    except UnicodeDecodeError:
        print("Invalid text encoding.")
        return None

    except OSError as e:
        print(f"File error: {e}")
        return None


def word_freq(text):
    words = text.split()
    freq = {}

    for word in words:
        word = word.lower()

        if not any(char.isalpha() for char in word):
            continue

        elif word in freq:
            freq[word] += 1

        else:
            freq[word] = 1

    for word, count in freq.items():
        print(f"{word}: {count}")

    return freq


# Main program

while True:
    user_input = input(
        "\nDo you want to analyze a text file? (yes/no): "
    ).strip().lower()

    if user_input == "yes":
        text = file_type_detector()

        if text is not None:
            result = word_freq(text)

    elif user_input == "no":
        print("Program terminated.")
        break

    else:
        print("Invalid input. Please enter yes or no.")
