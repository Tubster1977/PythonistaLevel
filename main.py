from python_art import logo
from python_buzzwords import buzzwords_list

print("Welcome to the Pythonista score calculator! \n")
print(logo)

# just as before, set score to 0
Score = 0

numberOfYearsOfExperience = []
numberOfYearsOfExperience.append(int(input("Years in web frameworks development? \n")))
numberOfYearsOfExperience.append(int(input("Years in object relational mapping? \n")))
numberOfYearsOfExperience.append(int(input("Years in python coding? \n")))
numberOfYearsOfExperience.append(int(input("Years in using django? \n")))
numberOfYearsOfExperience.append(int(input("Years in using sql? \n")))
numberOfYearsOfExperience.append(int(input("Years in machine learning? \n")))
# test - print(numberOfYearsOfExperience)
# print(type(numberOfYearsOfExperience[0]))

# determine the average number of years of experience across all desirable fields
def findAverageYearsOfExperience(numberOfYearsOfExperience):
  sumOfYears = sum(numberOfYearsOfExperience)
  totalEntries = len(numberOfYearsOfExperience)
  averageYearsOfExperience = sumOfYears / totalEntries
  return averageYearsOfExperience

# determine pythonista level
def findPythonistaLevel(averageYearsOfExperience):
  # Score has already been defined so has to be set to global
  global Score
  pythonistaLevel = ""
  if averageYearsOfExperience < 1:
    pythonistaLevel = "Beginner"
    Score += 0
  elif averageYearsOfExperience >= 1 and averageYearsOfExperience < 3:
    pythonistaLevel = "Intermediate"
    Score += 2
  elif averageYearsOfExperience >= 3:
    pythonistaLevel = "Expert"
    Score += 4
  return pythonistaLevel

averageYearsOfExperience = findAverageYearsOfExperience(numberOfYearsOfExperience)
print("Average no. of years of experience is: " + str(round(averageYearsOfExperience)))

pythonistaLevel = findPythonistaLevel(averageYearsOfExperience)
print("Your pythonista level is: " + pythonistaLevel)
print("Your basic score is: " + str(Score))

# create a dictionary using the values from the list with the keys being the fields

Fields = {"web-frame.devs", "obj.relat.map.", "python", "django", "sql", "mach.learn."}
yearsInDesirableFields = dict(zip(Fields, numberOfYearsOfExperience, strict=False))
#print(yearsInDesirableFields)

# iterate through dictionary & determine score for each field using on conditionals
for key, value in yearsInDesirableFields.items():
  if value < 1:
    Score += 0
    print(key + " - this field requires your attention! \n")
  elif value >= 1 and value < 3:
    Score += 2
    print(key + " - this field requires attention but you are making progress. \n")  
  elif value >= 3:
    Score += 4
    print(key + " - you are a proficient in this field, well done. \n")

# buzzword test

end_of_game = False
lives = 3

attempted = []

while not end_of_game:
  guess = input("Guess a buzzword (you have three lives): ").lower()
  if guess in buzzwords_list and guess not in attempted:
    print("Correct! \n")
    Score += 0.05
    attempted.append(guess)
  elif guess in attempted:
    print("You have already attempted this buzzword. \n")
  else:
    lives -= 1
    print("Incorrect! Lose a life! \n")
    if lives == 0:
      end_of_game = True
      print("You have no more lives left! \n")

# determine the overall score
#print("Your overall Pythonista score is: " + str(round(Score, 2)))
print("Your overall Pythonista score is: {:0.2f}".format(Score))

# check out some important Pythonista buzzwords
print("Here are some important Pythonista buzzwords: \n")

for i, val in enumerate(buzzwords_list):
  print(i + 1, val)
