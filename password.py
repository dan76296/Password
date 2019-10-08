import random

def random_char_password():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    upperalphabet = alphabet.upper()
    pw_len = 8
    pwlist = []

    for i in range(pw_len//3):
        pwlist.append(alphabet[random.randrange(len(alphabet))])
        pwlist.append(upperalphabet[random.randrange(len(upperalphabet))])
        pwlist.append(str(random.randrange(10)))
    for i in range(pw_len-len(pwlist)):
        pwlist.append(alphabet[random.randrange(len(alphabet))])

    random.shuffle(pwlist)
    pwstring = "".join(pwlist)
    print('\n')
    print('\t ' + pwstring)

filename = 'dictionary.txt'
def dict_password():
    item_list = open(filename, 'r')
    items = item_list.read().split()[0:]
    word_list = []
    for item in items:
        for letter in item:
            if letter.isdigit() == False:
                word_list.append(item)
    
    random.shuffle(word_list)
    pwstring = random.choice(word_list)
    
    numbers = range(0,20)
    special_chars = ['!', '@', "$", "%", "^", "&", "*", "(", ")", "-", "="]

    number = str(random.choice(numbers))
    char = random.choice(special_chars)

    password = pwstring + number + char
    print('\n')
    print('\t' + password)

print("====================================")
print('\n')

print("PASSWORD GENERATOR 2000")
print("\t 1. Random string")
print("\t 2. Dictionary word (Number and Special Character")
user_choice = input('\t > ')

if user_choice == '1':
    random_char_password()

if user_choice == '2':
    dict_password()

print('\n')
print("====================================")
