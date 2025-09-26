class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        result = []
        path =[]

        def backtrack(start: int) -> list:
            
            if len(path) == k:
                result.append(path[:])
                return


            max_start_length = n - (k-len(path))+1
            for x in range(start,max_start_length+1):
                path.append(x)
                backtrack(x+1)
                path.pop()

        backtrack(1)
        return result
