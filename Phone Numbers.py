import string
address_list = open("PhoneNumbers",'r')

for line in address_list:
    a = line.translate(str.maketrans('', '', string.punctuation))
    a = ''.join(a.split())
    line = ("({})-{}-{}".format(a[:3],a[3:6],a[6:]))
    f = open("PhoneNumbers","w")
    f.write(line)
    f.write('\n')
