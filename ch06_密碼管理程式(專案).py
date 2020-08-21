'''
密碼管理程式(專案)
'''

import sys
import pyperclip
password = {'email':'dasdasdasfaf846',
            'blog':'4d6f4gs5dg8rh6js',
            'fb':'5fdgfdvgAWAffg'}

if len(sys.argv) < 2:
    print('Usage: python 密碼管理程式(專案) [account] - copy account password')
    sys.exit()
    
account = sys.argv[1]

if account in password:
    pyperclip.copy(password[account])
    print('Password for '+ account +' copide to clipbord' )
else:
    print('There is no account name '+account)

print(pyperclip.paste())