class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        chain = path.split('/')
        for ch in chain:
            if ch == '' or ch == '.':
                continue
            if ch == '..':
                if stack:
                    stack.pop(-1)
            else:
                stack.append(ch)
        return '/' + '/'.join(stack)
            
                