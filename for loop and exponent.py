for letter in 'Python':
    if letter == 'h':
        continue
    print('Current Letter :', letter)

for letter in 'craftophobia':
    print(letter)

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)

for index in range(len(friends)):
    print(friends[index])


def raise_power(base, power):
    result = 1  
    for index in range(power):
        result = result * base 
    return result

print(raise_power(2,3))