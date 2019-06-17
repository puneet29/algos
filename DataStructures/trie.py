from collections import defaultdict


class Node:
    def __init__(self, val):
        self.data = val
        self.isTerminal = False
        self.hashmap = defaultdict(str)


class Trie:
    def __init__(self):
        self.root = Node(None)

    def addWord(self, word):
        temp = self.root
        for i in range(len(word)):
            ch = word[i]
            if(not temp.hashmap[ch]):
                child = Node(ch)
                temp.hashmap[ch] = child
                temp = child
            else:
                temp = temp.hashmap[ch]
        temp.isTerminal = True

    def search(self, word):
        temp = self.root
        for i in range(len(word)):
            ch = word[i]
            if(temp.hashmap[ch]):
                temp = temp.hashmap[ch]
            else:
                return False
            print(temp.data, end=" ")

        print()
        return(temp.isTerminal)


words = ["apple", "ape", "no", "not", "coder", "coding"]
t = Trie()

for i in range(6):
    t.addWord(list(words[i]))

searchWord = input()

if(t.search(searchWord)):
    print(searchWord, "is in trie")
else:
    print(searchWord, "is not in trie")
