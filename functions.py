

def sum(a, b=3.14):
  x = a + b
  sorted_num = sorted([a, b])
  return x, sorted_num
  print("Sum equals: ")
sum(4,5)
sum(4)

def sum1(a, b=3.14, verbose=False):
  x = a + b
  sorted_num = sorted([a, b])
  if verbose:
    print(f'Num1:{a},Num2{b}')
    print(f'Sum: {x}')
    print(f'Sorted Nums: [sorted_num]')

  return x, sorted_num
  print("Sum equals: ")
sum1(4,5)
sum1(4, verbose=True)


if __name__ == '__main__':
  
  sum(7, 19)
  sum1(2,19, verbose=True)

  help(function)