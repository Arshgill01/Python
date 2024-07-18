import re 
email = input("Whats your email? - ")
if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|net)$", email, re.IGNORECASE):
  print("Valid")
else:
  print("Invalid") 