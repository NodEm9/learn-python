import os

# r = Read
# a = Append
# w = Write
# x = Create


f = open("context.txt", "r")
# print(f.read())
# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()


try:
    f = open("name.txt", "r")
    print(f.read())
except: print("An error occurred: file does not exist")
finally: f.close()

# Append the file if it does not exist
f = open("name.txt", "a")
f.write("Alex")
f.close()

f = open("name.txt", "r")
print(f.read())
f.close()


# # Create a file if it does not exist
# f = open("employee.txt", "x")
# f.write("Alex")
# f.close()

if not os.path.exists("employee.txt"):
    f = open("employee.txt", "x")
    f.write("Alex")
    f.close()

# Write to a file (overwrite)
# f = open("employee.txt", "w")
# f.write("Content in the file has been overwritten")
# f.close()

# f = open("employee.txt")  
# print(f.read())
# f.close()



# Delete a file
if os.path.exists("employee.txt"):
    os.remove("employee.txt")
else:
    print("file does not exist")


with open("context.txt", "r") as f:
    content  = f.read()

with open("name.txt", "w") as f:
    f.write(content)
 
