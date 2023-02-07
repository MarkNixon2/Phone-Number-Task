import string

s = input("Enter phone number:")
a = s.translate(str.maketrans('', '', string.punctuation))
a = ''.join(a.split())
line = ("({})-{}-{}".format(a[:3],a[3:6],a[6:]))
f = open("PhoneNumbers","w")
f.write(line)
f.write('\n')
