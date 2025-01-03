class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        digit_to_letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        res = []

        def dfs(prefix, remaining):
            if len(remaining) == 0:
                res.append(prefix)
                return
            
            for letter in digit_to_letters[remaining[0]]:
                dfs(prefix + letter, remaining[1:])

        dfs('', digits)
        
        return res
