class Solution:
    def f(self, n, mem) -> int:
        if n <= 1:
            return n

        if n in mem:
            return mem[n]

        result = self.f(n - 1, mem) + self.f(n - 2, mem)
        mem[n] = result

        return result

    def fib(self, n: int) -> int:
        mem = {}
        return self.f(n, mem)