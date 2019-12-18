'''
# Crypto Challenges

## Challenge 1 – the Caesar cipher
Your challenge is to decipher this string: MYXQBKDEVKDSYXC

'''

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

str_in = 'MYXQBKDEVKDSYXC'
shift = 16
n = len(str_in)
str_out = ''
for i in range(n):
    c = str_in[i]
    loc = alpha.find(c)
    new_loc = (loc + shift)%26
    str_out += alpha[new_loc]
print(f'Garbled, {str_out}')