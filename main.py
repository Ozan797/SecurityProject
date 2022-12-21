import random

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!@#$%^&*()'
numbers = '1234567890'
all = lower_case + upper_case + symbols + numbers
length = 18
password = ''
for i in range(length):
    password += random.choice(all)
print(password)

account = 'Ozan'
org = input('Enter the organization name: ')
print(f'Password for {account} is {password} for {org}')


def write_to_file(account, org,password):
    with open('passwords.txt', 'a+') as f:
        f.write(account + '      ' + org + '      ')
        f.write(password + '\n')
        f.close()

if __name__ == '__main__':
    if org in open('passwords.txt').read():
        print('Account already exists')
    else:
        write_to_file(account,org,password)
