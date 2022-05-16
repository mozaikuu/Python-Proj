try:
 Name = input ("What is your name? ")
 age = input ("What is your age? ")
 if 18 <= int(age) :
  print ("Fuck you, " + name + "!" )
 elif int(age) > 18 : 
  print ("You are not old enough to fuck around, " + name + "!")
except :
  print("do you think im fucking dumb shithead? i may not be able to read but i know my numbers well and those arent fucking numbers. Go to math school, learn some numbers then come back and try again.")
#   print("i made this myself!") 
#   print("👌")  these dont work sadly ahmed 


def max_num(num1, num2, num3):
  if num1 >= num2 and num1 >= num3:
    return num1
  elif num2 >= num1 and num2 >= num3:
    return num2
  else:
    return num3

print(max_num(100, 20, 3))