class PrefixTree:

    def __init__(self):
        self.words = {}
        self.trie = {}
    def insert(self, word: str) -> None:
        self.words[word] = True
        for i in range(len(word)):
            self.trie[word[:i]] = True

    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        return (prefix in self.trie) or (prefix in self.words)
        