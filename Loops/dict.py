dict = {
  "Gryffindor": ["Hermione", "Harry", "Ron"], 
  "Slytherin": ["Draco"]
}

for key in dict: 
  for value in dict[key]: 
    print(value)
    
students = [
  {"name": "Harry", "house": "Gryffindor", "patronus": "otter"},
  {"name": "Hermione", "house": "Gryffindor", "patronus": "stag"}, 
  {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"}, 
  {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students: 
  for key in student: 
    print(f"{student[key]}, ", end="")
  print()