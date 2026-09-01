from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            current, steps = queue.popleft()

            if current == endWord:
                return steps

            for j in range(len(current)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == current[j]:
                        continue
                    next_word = current[:j] + c + current[j+1:]
                    if next_word in word_set and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, steps + 1))

        return 0