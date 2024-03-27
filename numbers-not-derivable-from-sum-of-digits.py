# This script prints out numbers that are impossible 
# to derive by dividing another number by the sum of its digits
# Below are some examples of how to derive the 
# numbers 1, 2, 3, 4, 5 by the sum of the digits of another number
# number    sum of digits     number/sum of digits
# 1         1                 1/1  = 1
# 18        1 + 8 = 9         18/9 = 2
# 27        2 + 7 = 9         27/9 = 3
# 12        1 + 2 = 3         12/3 = 4
# 45        4 + 5 = 9         45/9 = 5
# Note: to see numbers that are possible to derive in this way, 
# uncomment the second print statement
# Change the range in the 'numbers' variable for longer outputs

def split_digits_positive(num):
  digits = []
  while num > 0:
    digits.append(num % 10)
    num //= 10
  return digits[::-1]

def numbers_not_obtainable(numbers_list, results_list):
  for number in numbers_list:
    if not number in results_list:
      print(number)

def main():
  numbers = list(range(1, 1001))
  results = []
  for number in numbers:
    array_of_digits = split_digits_positive(number)
    sum_of_digits = sum(array_of_digits)
    result_float = number / sum_of_digits
    result_boolean = result_float.is_integer()
    if result_boolean:
      float_to_int = int(result_float)
      if not float_to_int in results:
        results.append(float_to_int)
        # print(f"{number} :      {float_to_int}")
  numbers_not_obtainable(numbers, results)

if __name__ == '__main__':
  main()

