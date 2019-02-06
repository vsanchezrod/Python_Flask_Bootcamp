print("------- OPERATORS --------")
print(1 > 2)
print(3 < 2)
print(1 >= 1)
print(3 <= 2)
print(3 == 3)
print(3 != 3)

username = "Admin"
check = "Admin"
permission = False

# Check equality
print(username == check)

print("------- MULTIPLE --------")
print(1 == 1 and 2 < 3)
print(1 == 1 or 2 < 3)
print(1 == 1 or 2 < 3 or 4 == 4)

print(username == check and permission)
permission = True
print(username == check and permission)