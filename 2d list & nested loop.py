number_grid =[
    [0, 1, 2],
    [3, 4, 5], 
    [6, 7, 8],
    [9]
 ]
 
print(number_grid[0][1])

number_grid =[
    [0, 1, 2],
    [3, 4, 5], 
    [6, 7, 8],
    [9]
 ]

for row in number_grid:
     for col in row:
         print(col)


def translate (phraze):
    translation = ""
    for letter in phraze:
        if letter in "Rr":
            if letter.isupper():
                translation = translation + "W"
            else:
                translation = translation + "w"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))