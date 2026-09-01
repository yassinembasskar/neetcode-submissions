class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        dictionnary = {}

        for a in prerequisites:
            if a[0] not in dictionnary:
                dictionnary[a[0]] = set()
            dictionnary[a[0]].add(a[1])
        res = []
        current = set()
        def dfs(num, current):
            nonlocal res
            if num in current:
                return False
            if num in visited:
                return True
            if num not in dictionnary:
                res = [num] + res
                visited.add(num)
                return True
            else:
                visited.add(num)
                current.add(num)
                for a in dictionnary[num]:
                    if not dfs(a, current):
                        return False
                current.remove(num)
                res.append(num)
                return True
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i, set()):
                    return []
        return res
                


