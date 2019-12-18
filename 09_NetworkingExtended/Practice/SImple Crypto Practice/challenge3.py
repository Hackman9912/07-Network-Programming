'''
# Crypto Challenges
 

## Challenge 3 – XOR

### The first challenge is here:

Decipher this: kquht}

Key is a single digit

###  Here's a longer example that is in a hexadecimal format:

Decipher this: 70155d5c45415d5011585446424c

Key is two digits of ASCII
'''

def decode(t,k):
    n = len(t)
    word = ''
    for i in range(n):
        a = t[i]
        b = k[i % len(k)]
        x = ord(b) ^ ord(a)
        word += chr(x)
        # print(t, k, x, chr(x))
    return word

def decode2(text, key):
    n = len(text)
    clear = ''
    for k in key:
        for i in range(n):
            t = text[i]
            x = ord(k) ^ ord(t)
            clear += chr(x)
    print(k,clear)
    return clear


# text = "kquht}"
# key = '8'
# word = decode(text, key)
# print(word)

count = 0
smash = bytearray.fromhex('70155d5c45415d5011585446424c').decode()
print(smash)
word1 = decode2(smash, '14')


print(f'word1 {word1}')
# while count < 100:
    

