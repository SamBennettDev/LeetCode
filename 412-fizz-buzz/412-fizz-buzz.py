class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out = []
        for i in range(1, n + 1):
            ans = ("" if i % 3 else "Fizz") + ("" if i % 5 else "Buzz") or str(i)
            out.append(ans)
        return out