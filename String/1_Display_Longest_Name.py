from typing import List

class Solution:
    def longest(self, n: int, names: List[str]) -> str:
        longest_name = ""
        max_length = 0
        
        for name in names:
            if len(name) > max_length:
                longest_name = name
                max_length = len(name)
        
        return longest_name

sol = Solution()

n1 = 5
names1 = ["Geek", "Geeks", "Geeksfor", "GeeksforGeek", "GeeksforGeeks"]
print(sol.longest(n1, names1))  # Output should be "GeeksforGeeks"

n2 = 4
names2 = ["Apple", "Mango", "Orange", "Banana"]
print(sol.longest(n2, names2))  # Output should be "Orange"
