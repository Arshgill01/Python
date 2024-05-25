def main():
  x = int(input("What's x? "))
  if is_even(x):
    print("Even")
  else:
    print("Odd")

def is_even(n):
  return n % 2 == 0 # The func of THIS function is TO SPECIFICALLY find IF EVEN OR NOT, no need of if else


main()
