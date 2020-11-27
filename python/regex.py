import re
data = "Hello. My email is panditpg@mail.uc.edu. Please contact me!"
##p = re.compile('[A-Za-z0-9_%.-]+@[A-z0-9_%.-]+\.[A-z0-9]{2,}')
p = re.compile('[A-z0-9_%.-]+@[A-z0-9_%.-]+\.(com|net|org|ninja|edu)+')
print(p.search(data).group())
