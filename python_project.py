x = input("Enter phone number:")
y = x.replace(" ", "")
z = y.replace(")", "")
a = z.replace("(", "")
b = a.replace("-", "")
print(b)

num = "(" + b[0:3] + ")" + " " + b[3:6] + "-" + b[6:10]
print(num)
