#multi line strings
string="""hello 
my name is Sneha
byee
"""
print(string)

#indexes in string
st1="I love Python"
print(st1[0])
print(st1[-1])

# string slicing
print(st1[0:6])
print(st1[0:])
print(st1[-13:])

#string methods

print(st1.upper())
print(st1.lower())
print(st1.count('o'))#gives the no of times o appears in the string
print(st1.find('o'))#gives the index where o first appears

#replace
new_str=st1.replace('Python','Java')
print(new_str)

#concatenating 
greet="hello"
name="sneha"

print(greet+name)#using '+' operator

message='{},{} WELCOME!'.format(greet,name)#using .format method
print(message)

#fstrings
print(f"{greet},{name} WHAT'S UP?")

#TO SEE ALL THE ATTRIBUTES AND METHODS ASSOCIATED WITH THE VARIABLE
name1="sneha"
print(dir(name))

#to get the info and description of all methods of str class-> use help()

print(help(str))


# to display the built-in documentation specifically for the .lower() string method, followed by None

print(help(str.lower))