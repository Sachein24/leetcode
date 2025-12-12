class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        i = 1
        op = []

        while i <= n:
            if i % 3 == 0 and i % 5 == 0:
                op.append("FizzBuzz")
            elif i % 3 == 0:
                op.append("Fizz")
            elif i % 5 == 0:
                op.append("Buzz")
            else:
                op.append(str(i))

            i += 1

        return op
