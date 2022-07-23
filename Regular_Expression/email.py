import re

emails = '''
PythonDevs@gmail.com
hello.WoRld@university.edu
I-am-Boss-321@my-work.net
'''

pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

matches = pattern.finditer(emails)

for match in matches:
    print(match)