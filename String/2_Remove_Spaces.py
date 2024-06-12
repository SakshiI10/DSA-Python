class Solution:
    def modify(self, s: str) -> str:
        result = ""
        for char in s:
            if char != ' ':
                result += char
        return result

# Example usage:
sol = Solution()

s1 = "geeks  for geeks"
print(sol.modify(s1))  # Output should be "geeksforgeeks"

s2 = "    g f g"
print(sol.modify(s2))  # Output should be "gfg"
