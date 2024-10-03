"""My solution to the classic fizzbuzz question."""


fizzbuzz = lambda x: 'FizzBuzz' if x%15 == 0 else 'Fizz' if x % 3 == 0 else 'Buzz' if x % 5 == 0 else str(x)
print([fizzbuzz(i) for i in range(1,100)])