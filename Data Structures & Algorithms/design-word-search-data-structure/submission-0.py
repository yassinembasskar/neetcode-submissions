class WordDictionary:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_word = False

    def __init__(self):
        self.root = self.TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if not char in node.children:
                node.children[char] = self.TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word) - 1:
                if word[i] == '.':
                    for child in node.children.values():
                        if child.is_word:
                            return True
                    return False
                return (word[i] in node.children) and node.children[word[i]].is_word

            if word[i] != '.' and word[i] not in node.children:
                return False
            if word[i] != '.': 
                return dfs(i+1, node.children[word[i]])
            else:
                if not node.children:
                    return False
                for child in node.children.values():
                    if dfs(i+1, child):
                        return True
                return False
        
        return dfs(0, self.root)
                    
