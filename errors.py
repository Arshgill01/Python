while True:
    x = input("What's x? ")
    try:
      x = int(x)
      break
    except ValueError:
      print("x is not an integer")
print(f"x is {x}")

