import re, pyperclip



phoneRegex = re.compile(r'''(
(\d{3}|(\d{3}\))?
(\s|-|\.)?
(\d{3})
(\s|-|\.)
(\d{4})
(\s*(ext|x|ext.)\s*(|d{2,5}))?
)''', re.VERBOSE)



emailRegex = re.compile(r'''(
[a-zA-Z0-9.+-%]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2,4})        
)''',re.VERBOSE)


text = str(pyperclip.paste())
match = []
for groups in phoneRegex.findall(text):
    phonenum = '-'.join(groups[1],groups[3],groups[5])
    if groups[8] != '':
        phonenum += ' x' + groups[8]
    match.append(phonenum)
    
for groups in emailRegex.findall(text):
    match.append(groups[0])
    
if len(match) > 0:
    pyperclip.copy('\n'.join(match))
    print('Copied to clipboard')
    print('\n'.join(match))
else:
    print('NO FOUND')