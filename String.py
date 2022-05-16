print("Generic Text")  #normal text
print("generic\ntext") #newline
print("generic\"text") #anything after "\" is escaped literally 
phraze = "Wubba Lubba Dub Dub " #store string as variable
print(phraze)
print(phraze + "Generic Text") #concatenate (link together) strings
print(phraze.lower()) #lowercase #can also use .upper()
print(phraze.islower()) #returns boolean
print(phraze.upper().isupper()) #the .upper is done and used by isupper to return boolean and is hidden 
print(len(phraze)) #returns length of string
print(phraze [0]) #returns first character
#index starts from zero do not forget
# Wubba Lubba Dub Dub
# 0123456789
print(phraze.index("Dub")) #returns index of first occurence of Dub
print(phraze.replace("Dub", "Dubby")) #replaces Dub with Dubs
print(phraze.replace("Wub", "Wubby").replace("Dub", "Dubby").replace("Lub", "Lubby"))#replace multiple occurences of wub with wubby and replace dub with dubby and lub with lubby 

