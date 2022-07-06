import phonemes
import re

# reads in data from the text file to initialize the Trie
def get_from_file():
    pattern = re.compile("\d*\s+")
    words = phonemes.Trie()
    with open("cmudict-0.7b.txt", 'r') as input:
        for line in input:
            word = pattern.split(line)
            del word[-1]
            del word[0]
            words.insert(word)
        
    return words

def main():
    words = get_from_file()
    #print(words.get_words())
    print(words.get_containing(["HH", "AH", "T"]))

if __name__ == "__main__":
    main()