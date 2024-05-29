def main():
  time = input("What's the time? ")
  hours , minutes , ampm = map (int , time.split(":"))
  determine_time_of_day = convert(hours, minutes)
  ampm = decide(ampm)
  


  if 00 <= determine_time_of_day < 12:
    print("Morning")
  elif 12 <= determine_time_of_day < 18:
    print("Afternoon")
  elif 18 <= determine_time_of_day < 22:
    print("Evening")
  else:
    print("Night")
  def convert(hours, minutes):
    return hours + minutes / 60.0
  def decide(ampm):
    if 0 <= time < 12:
      return am

  
  





main()