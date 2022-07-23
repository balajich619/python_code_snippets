
import re

urls = '''
https://www.google.com
http://github.com
https://youtube.com
https://www.amazon.in
'''

pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
matches=pattern.finditer(urls)

for match in matches:
    print(match)
    
#using groups()

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)') 
matches=pattern.finditer(urls)

for match in matches:
    print(match.group(2) + match.group(3))
    
'''
expected O/P:
google.com
github.com
youtube.com
amazon.in
'''

#using sub
subbed_url=pattern.sub(r'\2\3',urls)

print(subbed_url)