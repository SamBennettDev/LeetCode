class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        int_list = list(map(int, str(x)))
        list_len = len(int_list)
        for i in range(list_len // 2):
            if int_list[i] != int_list[list_len - i - 1]:
                return False
        return True
        
        