import argparse, fileinput, itertools, time
# import ipdb; ipdb.set_trace()


def parser():
    parser = argparse.ArgumentParser(description='This is an anagram solver')
    parser.add_argument('-w',
                        "--word",
                        help='Input a word',
                        required=True
                        )
    parser.add_argument('-e',
                        "--exact",
                        help='Word matches have to be exact length',
                        required=False,
                        action='store_true'
                        )
    args = parser.parse_args()
    return args


def stripper(args):
    anagram = args.word
    print '{} letter anagram'.format(len(anagram))
    filein = fileinput.input(['a-z'])
    word_list = list(anagram)
    new_dict = []

    for letter in word_list:
        for line in filein:
            clean_word = line.rstrip().lower()
            if args.exact:
                if len(clean_word) == len(anagram) and letter in clean_word:
                    new_dict.append(clean_word)
            else:
                if len(clean_word) <= len(anagram) and letter in clean_word:
                    new_dict.append(clean_word)

    print 'Dictionary is {} words long'.format(len(new_dict))
    return new_dict


def wordchecker(new_dict, anagram):
    word = anagram.word
    wordlist = list(word)
    combos = set([''.join(combo)
                 for combo in set(itertools.permutations(wordlist))]
                 )
    tries = 0
    match = 0

    for d in new_dict:
        if any(d in combo for combo in combos):
            match += 1
            print 'Match found: ' + d
        tries += 1

    checks_per_second = (tries * len(new_dict)) / time.clock()
    print '{} matches found out of {} combinations in {} seconds\n{} checks per second'.format(
        match,
        tries,
        time.clock(),
        checks_per_second,
        )


def main():
    time.clock()
    anagram = parser()
    new_dict = stripper(anagram)
    wordchecker(new_dict, anagram)


if __name__ == "__main__":
    main()
