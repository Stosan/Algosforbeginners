#fizzbuzz algorithm
"""
1. if the input is divisible 3, return fizz
2. if the input is divisible by 5, return buzz
3. if the input is divisible by 3 & 5, we get fizzbuzz
4. any other number return same number
"""
def fizzbuzz(input):
    if (input % 3 ==0) and (input % 5 ==0):
         return "fizzbuzz"
    if input % 3 ==0:
        return "fizz"
    if input % 5 ==0:
        return "buzz"
    return input

print(fizzbuzz(2))