import argparse, fileinput, itertools


def parser():
    parser = argparse.ArgumentParser(description='This is an anagram solver')
    parser.add_argument('-w',
                        "--word",
                        help='Input a word',
                        required=True)
    args = parser.parse_args()
    return args


def stripper(string):
    string = string.word
    filein = fileinput.input(['words'])
    new_dict = []
    for line in filein:
        clean_word = line.rstrip()
        if len(clean_word) <= len(string):
            new_dict.append(clean_word)

    # wordlist = list(string)
    # alpha = string.lowercase
    # for l in wordlist:
    #     alpha = alpha.replace(l, '')
    return new_dict


def wordchecker(new_dict, string):
    for word in new_dict:
        if string == word:
            return True
    return False


def word_list(new_dict, string):
    word = string.word
    wordlist = list(word)
    combos = itertools.permutations(wordlist)
    for combo in combos:
        new_word = ''.join(combo)
        if wordchecker(new_dict, new_word):
            print 'Match found: ' + new_word
        else:
            print 'No match found: ' + new_word


def main():
    string = parser()
    new_dict = stripper(string)
    word_list(new_dict, string)


if __name__ == "__main__":
    main()
