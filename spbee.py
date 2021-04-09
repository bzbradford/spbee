from sys import argv
import re


def load_words():
    with open('dictionary.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


def main(argv):
    letters = argv[1]

    result = []
    with open('dict/dictionary.txt', 'r') as words_file:
        for line in words_file:
            word = line.strip()
            if can_spell(letters, word):
                result.append(word)

    result = sorted(result, key=lambda w: len(w), reverse=True)

    for word in result:
        print(word)

if __name__ == '__main__':
    main(argv)

if __name__ == '__main__':
    english_words = load_words()
    # demo print
    print('fate' in english_words)