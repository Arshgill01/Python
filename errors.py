def main():
  x = get_number("Waht")
  print(f"x is {x}")

def get_number():
    while True:
        try:
          return int(input("What's x? "))
          
        except ValueError:
          print("x is not an integer") ## pass can be used too, if you don't wanna keep on prompting user with "x i s not an integer"
          
        
        ## also else: break
        ## in functions there's not much need of break, instead we can simply use return(as we'll be using it either way)



main()
