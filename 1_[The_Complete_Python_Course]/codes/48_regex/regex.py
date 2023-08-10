# [a-z] means set a to z any character
# [a-z]+ means set a to z any character repeating

import re

validator = "[a-z]+@([a-z]+\.com)"
# validator = "[a-z]+@([a-z]+\.com)"

emails = "abc@gmail.com fgh@gmail.com vyg@gmail.com"
matches = re.findall(validator, emails)

print(matches)

email = "abc@ymail.com"
match = re.search(validator, email)


print(match.group(0))
#  can be used to get domains
print(match.group(1))
