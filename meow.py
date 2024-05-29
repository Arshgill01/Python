def main():
  number = get_number()
  meow(number)
  
def get_number():
  n = int(input("Whats n? "))
  while True:
    if n > 0:
      return n

def meow(n):
  for _ in range(n):
    print("meow")

main()
