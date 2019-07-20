import re

regex_user = '^(?=(?:.*[a-z]))(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{5,9}'
print('username :')
username = input()
print('is_username_valid',bool(re.search(regex_user, username)))

regex_pass = '(?=(?:.*[a-z]))(?=.*[$=_]{1})(?=.*[A-Z]{1})(?=.*[0-9]{1})(?=.*[$=_])[a-zA-Z0-9$=_$=_]{8,}'
print('password :')
password = input()
print('is_password_valid',bool(re.search(regex_pass, password)))