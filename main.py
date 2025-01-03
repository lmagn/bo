def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words = word_count(file_contents)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{num_words} words found in the document")
        words = "ajkl"
        num_letters = letter_count(file_contents, words)
        for value in num_letters:
            print(f"The '{value}' character was found {num_letters[value]} times")

        print("--- End report ---")

def word_count(file):
    file = str(file)
    words = file.split()
    return len(words)

def letter_count(contents, string):
    file = contents.lower()
    dict = {}
    for char in string.lower():
        dict[char] = 0


    for char in file:
        if char in dict:
            dict[char] += 1
    return dict

def on_sort(dict):
    return dict.sort




main()
