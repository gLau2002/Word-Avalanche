class Node:
    # each node in the Trie has a dictionary mapping phonemes to more nodes
    # is_end indicates that the phonemes from the root to this node forms a word
    def __init__(self) -> None:
        self.children = {}
        self.is_end = False

class Trie:
    # phonemes = ["AA", "AE", "AH", "AO", "AW", "AY", "B", "CH",
    # "D", "DH", "EH", "ER", "EY", "F", "G", "HH", "IH", "IY", "JH",
    # "K", "L", "M", "N", "NG", "OW", "OY", "P", "R", "S", "SH", "T",
    # "TH", "UH", "UW", "V", "W", "Y", "Z", "ZH"]

    def __init__(self) -> None:
        self.root = Node()

    # inserts a list of phonemes (word) into the Trie
    def insert(self, word):
        node = self.root
        for phoneme in word:
            if phoneme not in node.children:
                node.children[phoneme] = Node()
            node = node.children[phoneme]
        node.is_end = True

    # returns true if word is in the Trie (where word is a list of phonemes)
    def search(self, word):
        node = self.root
        for phoneme in word:
            if phoneme not in node.children:
                return None
            node = node.children[phoneme]
        return node if node.is_end else None
    
    # deletes a word from the Trie
    def delete(self, word):
        def rec(node, word, i):
            if i == len(word):
                node.is_end = False
                return len(node.children) == 0
            else:
                next_deletion = rec(node.children[word[i]], word, i+1)
                if next_deletion:
                    del node.children[word[i]]
                return next_deletion and not node.is_end and len(node.children) == 0

        if self.search(word):
            rec(self.root, word, 0)

    # returns a list of strings where each string is a word in the Trie
    def get_words(self):
        def rec(node, word, word_list):
            if node.is_end:
                word_list.append("".join(word))
            for phoneme in node.children:
                word.append(phoneme)
                rec(node.children[phoneme], word, word_list)
                word.pop()
        
        word_list = []
        rec(self.root, [], word_list)
        return word_list

    # returns all words containing characters in a list of phonemes
    def get_containing(self, phonemes):
        def rec(node, word, word_list):
            if node.is_end:
                word_list.append("".join(word))
            for phoneme in node.children:
                if phoneme not in phonemes:
                    continue
                word.append(phoneme)
                rec(node.children[phoneme], word, word_list)
                word.pop()

        word_list = []
        rec(self.root, [], word_list)
        return word_list
    
def main():
    myTrie = Trie()
    myTrie.insert(["TH", "R", "IY", "D", "IY"])
    myTrie.insert(["B", "AO", "T", "S"])
    myTrie.insert(["B", "AO", "B", "T", "AO", "T"])
    print(myTrie.get_words())
    print(myTrie.get_containing(["B", "AO", "T", "S"]))

if __name__ == "__main__":
    main()

    