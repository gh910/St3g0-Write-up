# St3g0-Write-up

Description :
my friend color challenged me to get the flag but i'm very bad at steganography so help me get it 

This challenge was created by taking a flag, splitting it into individual characters, and adding 1 to a random color channel in a pixel in a section. 

![stego](https://user-images.githubusercontent.com/80649768/189890669-59d4f7dc-0f3e-4096-9ae9-edbb4b278b90.png)


The challenge can be solved by guessing the appropriate length of the flag, adding all the differences in each section to create a letter from the ASCII code, and seeing if it matches our flag format. (See Solve.py )
