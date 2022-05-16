from ssl import DefaultVerifyPaths


lucky_numbers = [1, 3, 7, 49, 69, 420]
friends = ["khalid", "youssef", "youssef", "khalid", "youssef"] # list of strings   can use numbers and boolean values
print(friends) #this sounds so sad but it works
print(friends[0]) # prints the first element of the list
print(friends[-1]) # prints the last element of the list
print(friends[1:]) # prints the second element to the end of the list
print(friends[1:3]) # prints the second element to the third element of the list
print(friends[:3]) # prints the first element to the third element of the list
print(friends[::2]) # prints every other element of the list
print(friends[::-1]) # prints the list in reverse order
friends[0] = "youssef" # changes the first element of the list

friends.extend(lucky_numbers) # adds the lucky numbers to the end of the list
print(friends)
friends.append("khalid") # adds khalid to the end of the list
print(friends)
friends.insert(1, "youssef") # inserts youssef at the second position of the list
print(friends)
friends.remove("youssef") # removes youssef from the list
print(friends)
friends.pop() # removes the last element of the list
print(friends)
friends.pop(1) # removes the element at the second position of the list
print(friends)
friends.clear() # removes all elements of the list
print(friends)
friends.sort() # sorts the list in ascending order
print(friends)
friends.sort(reverse=True) # sorts the list in descending order 
friends.reverse() # reverses the list
print(friends)
friends.reverse() # reverses the order of the list
print(friends)
print(friends.index("khalid")) # prints the index of khalid
print(friends.count("khalid")) # prints the number of times khalid appears in the list
print(friends)

friends2 = friends.copy() # copies the list

davey = friends.sort(reverse=True) 
print(davey) #also doesnt work...