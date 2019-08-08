import re

a = "python3 dz 9"
r = re.findall("[d-z][0-9]", a)
print(r)

