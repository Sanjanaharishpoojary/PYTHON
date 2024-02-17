password={'google':'qwerty789','fb':8905567,'chrome':'sanja@123'}
import sys.pyperclip
if len(sys.argv)<2:
    print('usage:py pw.py[account]-copy account password')
    sys.exit()
account=sys.argv[1]
if account in passwords:
    pyperclip.copy(password[account])
    print('password'+account+'copied to clipboard.')
else:
    print('there is no account named'+account)