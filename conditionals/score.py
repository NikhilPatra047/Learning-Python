score = int(input("Enter score: "))
if score > 100: 
  score = 100 

if score >= 90 <= 100: 
  print("Grade A")
elif score >= 80 < 90: 
  print("Grade B")
elif score >= 70 < 80: 
  print("Grade C")
elif score >= 60 < 70:
  print("Grade D")
else:
  print("Grade F")