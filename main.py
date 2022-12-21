import random

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!@#$%^&*()'
numbers = '1234567890'
all = lower_case + upper_case + symbols + numbers
length = 24
password = ''
for i in range(length):
    password += random.choice(all)

email = input('Email Address : ')
org = input('Org : ')
print(f'Password for {email} is {password} for {org}')


def write_to_file(email, org,password):
    with open('passwords.txt', 'a+') as f:
        f.write(email + '      ' + org + '      ')
        f.write(password + '\n')
        f.close()

if __name__ == '__main__':
    if org in open('passwords.txt').read():
        print('email already exists')
    else:
        write_to_file(email,org,password)
