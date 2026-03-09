print("\n************Creating a Dictionary****************")
data = {"name": "Jake", "age": 22}
print(data)

# using dict() constructor
d2 = dict(a="Geeks", b="for", c="Geeks")
print(d2)

print("\n************Accessing Dictionary Items****************")
d = {"name": "Kat", 1: "Python", (1, 2): [1, 2, 4]}

# Access using key
print(d["name"])

# Access using get()
print(d.get("name"))

print("\n************Adding and Updating Dictionary Items****************")
d = {1: "Geeks", 2: "For", 3: "Geeks"}

# Adding a new key-value pair
d["age"] = 22

# Updating an existing value
d[1] = "Python dict"
print(d)

print("\n************Removing Dictionary Items****************")
d = {1: "Geeks", 2: "For", 3: "Geeks", "age": 22}

# Using del
del d["age"]
print(d)

# Using pop()
val = d.pop(1)
print(val)

# Using popitem()
key, val = d.popitem()
print(f"Key: {key}, Value: {val}")

# Using clear()
d.clear()
print(d)

print("\n************Iterating Through a Dictionary****************")
d = {1: "Geeks", 2: "For", "age": 22}

# Iterate over keys
for key in d:
    print(key)

# Iterate over values
for value in d.values():
    print(value)

# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")

d = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(d)

print("\n************Dictionary Comprehension****************")

sq = {x: x**2 for x in range(1, 6)}
print(sq)

print("\n***********Creating a Dictionary from Two Lists****************")
keys = ["a", "b", "c", "d", "e"]
values = [1, 2, 3, 4, 5]

d = {k: v for (k, v) in zip(keys, values)}
print(d)
