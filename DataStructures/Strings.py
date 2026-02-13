print("**************Multi-line Strings************")
s = """I am Learning
Python String on GeeksforGeeks"""
print(s)

s = '''I'm a 
Geek'''
print(s)

print("\n**************Accessing characters in String************")
s = "GeeksforGeeks"
print(s[0])   # first character
print(s[4])   # 5th character
print(s[-10])   # 3rd character
print(s[-5])    # 5th character from end

print("\n**************String Slicing************")
s = "GeeksforGeeks"
print(s[1:4])    # characters from index 1 to 3
print(s[:3])     # from start to index 2
print(s[3:])     # from index 3 to end
print(s[::-1])   # reverse string

s = "Hello, World!"
# Get the entire string
s2 = s[:]
s3 = s[::]
print(s2)
print(s3)

s = "abcdefghi"

# Every second character
print(s[::2])

# Every third character from index 1 to 8 (exclusive)
print(s[1:8:3])

print("\n**************Updating a String************")
s = "hello geeks"
s1 = "H" + s[1:]                   # update first character
s2 = s.replace("geeks", "GeeksforGeeks")  # replace word
print(s1)
print(s2)

print("\n**************upper() and lower()************")
s = "Hello World"
print(s.upper())
print(s.lower())

print("\n**************strip()************")
#removes leading and trailing whitespace from the string

s = "   Gfg   "
print(s.strip())    

s = "Python is fun"
print(s.replace("fun", "awesome"))



