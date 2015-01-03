import argparse

parser = argparse.ArgumentParser(description='This is an anagram solver')
parser.add_argument('-w',
                    "--word",
                    help='Input a word',
                    required=True)
args = parser.parse_args()
print args.word
