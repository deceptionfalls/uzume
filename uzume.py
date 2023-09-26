# Uzume. Small password generator
import random, string
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--length", default=10, required=False, type=int, help='Length of the generated password. Defaults to 10 characters')
parser.add_argument("-u", "--uppercase", action='store_true', required=False, help='Include uppercase letters')
parser.add_argument("-n", "--numbers", action='store_true', required=False, help='Include numbers')
parser.add_argument("-s", "--symbols", action='store_true', required=False, help='Include symbols')

args = parser.parse_args()

def randompass():
    length = args.length
    letters = string.ascii_lowercase

    if args.uppercase is True: # only uppercase
        letters = string.ascii_letters

    if args.symbols is True: # only symbols
        letters = string.ascii_lowercase+string.punctuation

    if args.numbers is True:   # only numbers
        letters = string.ascii_lowercase+string.digits

    if args.numbers and args.symbols is True:   # numbers and symbols
        letters = string.ascii_lowercase+string.digits+string.punctuation

    if args.numbers and args.uppercase is True:   # numbers and uppercase
        letters = string.ascii_letters+string.digits

    if args.uppercase and args.symbols is True: # uppercase and symbols
        letters = string.ascii_letters+string.punctuation

    if args.numbers and args.uppercase and args.symbols is True:   # numbers, uppercase and symbols
        letters = string.ascii_letters+string.digits+string.punctuation

    return ''.join(random.choice(letters) for i in range(length))

if __name__ == '__main__':
    print(f'\033[93m{randompass()}\033[0m')
