class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start = 0
        while start < len(arr)-1 and arr[start]<x:
            start+=1
        end = start+1
        if start-1 >= 0  and abs(arr[start-1]-x) <= abs(arr[start]-x):
            start = start-1
            end = start+1
        n = 1
        while n < k:
            if start-1 >= 0 and end < len(arr):
                if abs(arr[start-1]-x) <= abs(arr[end]-x):
                    start-=1
                else:
                    end+=1
            elif start-1 >= 0:
                start-=1
            elif end < len(arr):
                end+=1
            else:
                break
            n+=1
        return arr[start:end]
        

