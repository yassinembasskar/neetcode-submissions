class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_less(small, big):
            return any(k not in big or big[k] < small[k] for k in small)

        if len(t) > len(s):
            return ""

        small = {}
        for c in t:
            small[c] = small.get(c, 0) + 1
        big = {}
        results = {}
        left = 0 
        right = 0
        while right < len(s) or left < len(s):
            if right >= len(s):
                if is_less(small, big):
                    break
                else:
                    if s[left] not in small:
                        left += 1
                    else:
                        results[right - left] = (left, right)
                        big[s[left]]-=1
                        left +=1
            elif s[right] in small:
                if s[left] not in small:
                    left += 1
                else:
                    if is_less(small, big):
                        big[s[right]] = big.get(s[right], 0) + 1
                        right += 1
                    else:
                        results[right - left] = (left, right)
                        big[s[left]]-=1
                        left +=1
            else:
                if s[right-1] in small and not is_less(small, big):
                    results[right - left] = (left, right)
                    if s[left] in big:
                        big[s[left]]-=1
                    left +=1
                    continue
                right+=1

        if results:
            pair = results[min(results.keys())]
            return s[pair[0]: pair[1]]
        else:
            return ""

                

                