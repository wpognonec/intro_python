#Write Python code to replace all the : characters in the string below with +
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
new_info = ''

for char in info:
    new_info += char if char != ':' else '+'

print(new_info)
print(info.replace(':', '+'))