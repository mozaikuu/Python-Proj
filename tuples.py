#tuples are like lists data structures that are immutable 
coords = [(4, 5)] #list of tuples   list=[]  tuple=() dict={}
print(coords[0]) # prints the first element of the tuple
print(coords[1]) # prints the second element of the tuple
print(coords[-1]) # prints the last element of the tuple    
print(coords[-2]) # prints the second to last element of the tuple  

monthconversions = {  
    0: "January",
    1: "February",
    10: "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}    
print(monthconversions[0])  # prints January
print(monthconversions.get(0))  # prints January
print(monthconversions.get("Dec"))  # prints December
print(monthconversions.get("luv", "Not a valid key"))  # prints Not a valid key

i=1
while i<=10000:
    print(i)
    i+=1
print("done with loop") 

