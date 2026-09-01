class Solution:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.word = None
            

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = self.TrieNode()
        for word in words:
            node = root
            for char in word:
                if not char in node.children:
                    node.children[char] = self.TrieNode()
                node = node.children[char]
            node.word = word
        
        res = []
        def dfs(i, j, node, visited):
            if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0 or (i,j) in visited:
                return None
            if board[i][j] not in node.children:
                return None
            else:
                new_node = node.children[board[i][j]]
                if new_node.word:
                    res.append(new_node.word)    
                visited[(i, j)] = True
                dfs(i+1, j, new_node, visited)
                dfs(i-1, j, new_node, visited)
                dfs(i, j+1, new_node, visited)
                dfs(i, j-1, new_node, visited)
                del visited[(i, j)]
                if not new_node.children:
                    del node.children[board[i][j]]

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,root,{})
        
        return list(set(res))

                
            
                

