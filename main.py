
***
Now let us consider how to generate a random lowercase letter. The ASCII
code for lowercase letters are consecutive integers starting from the ASCII
code for 'a', then for 'b', 'c', ..., and 'z'. The ASCII code for 'a' is
ord('a')

 So, a random integer between ord('a') and ord('z') is

random.randint(ord('a'), ord('z'))
- And, a random lowercase letter is

chr(random.randint(ord('a'), ord('z')))

- To generalize the foregoing discussion, a random character between any two
characters ch1 and ch2 with ch1 < ch2 can be generated as follows:
chr(random.randint(ord(ch1), ord(ch2)))
***

def generating_random_characters():
    pass