number1 = int(input("Please enter the number - "))
number1_9_words = ["Zero","One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

for _ in range(1,10):
  if _ == number1:
    print(number1_9_words[_])
    break
else:
  print(number1)