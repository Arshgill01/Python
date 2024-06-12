def main():
  fuel_calculator()




def fuel_calculator():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = map(float, fraction.split("/"))

            if x > y or y == 0:
                break

            percentage = (x / y * 100)

            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            elif 24 < percentage < 26:  # Checking for percentage in the range (24, 26)
                print("25%")
            elif 49 < percentage < 51:  # Checking for percentage in the range (49, 51)
                print("50%")
            elif 74 < percentage < 76:  # Checking for percentage in the range (74, 76)
                print("75%")
            else:
              continue
            

            break  # Exit the loop after successfully processing the input
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


main()