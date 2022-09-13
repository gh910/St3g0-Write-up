from PIL import Image
from collections import Counter
import random
import re


stego = Image.open('./stego.png').convert()
pixels = stego.load()

main_color = Counter(pixels[i,j] for i in range(stego.size[0]) for j in range(stego.size[1])).most_common(1)[0][0]

def try_len(l):
    flag = ''
    width = stego.size[0]//l
    height = stego.size[1]//l
    for index in range(l):
        # Loop once per supposed char length
        count = 0
        for i in range(width*index, width*(index+1)):
            for j in range(height*index, height*(index+1)):
                count += sum(pixels[i,j][k]-main_color[k] for k in range(3))
        flag += chr(count)
    return flag


l = 1
while True:
    l += 1
    if l > stego.size[0]:
        break # We're done. No flag, I guess.
    flag = try_len(l)
    if not flag:
        continue
    if re.match(r'yuctf\{[0-9a-zA-Z_]*\}', flag):
        print(flag)
        break