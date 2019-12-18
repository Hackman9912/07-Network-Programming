'''
# Crypto Challenges


## Challenge 2 – base64

Decode this: VGhpcyBpcyB0b28gZWFzeQ==

## Challenge 2.1 - base64

Decode this: VWtkc2EwbEliSFprVTBjeFl6lZaMWxUUW5OaU1qbDNVSGM5UFFvPQo=

Hint: several rounds of Base64 were used. 


'''

import base64
import encodings
import codecs

def decoder(x,y):
    for _ in range(x):
        y = base64.b64decode(y + b'=')
    return y


decoded = base64.b64decode('VGhpcyBpcyB0b28gZWFzeQ==')
print(decoded.decode('ascii'))


value = r'VWtkc2EwbEliSFprVTBJeFl6SlZaMWxUUW5OaU1qbDNVSGM5UFE9PQ=='
decoded2 = base64.b64decode(value)
decoded2 = decoder(2, decoded2)
print(decoded2)