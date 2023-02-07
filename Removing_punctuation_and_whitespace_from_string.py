import string
s = "(420)   647-3944"
output = s.translate(str.maketrans('', '', string.punctuation))
output = ''.join(output.split())
print(output)