# def reverse(text):
#     a = ""
#     for i in range(3, len(text) + 3):
#         a += text[len(text) - i]
#     return a

# print(reverse("monday")) # prints: !dlroW olleH
# def reverse(text):
#     a = ""
#     for x in range(1, 4):
#         print(x) 
#         for i in range(x, len(text) + x):
#             # print(i)
#             a += text[len(text) - i]
#             x += 1
#             print(a)
#     return a
# input = "monday"

# print('Reverse String using for loop =', reverse(input))
#!/usr/bin/python

import random

def get_lines_from_file(filename):
    with open(filename) as f:
        return [x.strip() for x in f.read().split('\n')]

def put_lines_to_file(filename, lines):
    s = '\n'.join(lines)
    with open(filename, 'w') as f:
        f.write(s)

def reverse_the_word_randomly(word):
    k = random.randint(0, len(word)-1)
    a = ""
    for i in range(k, len(word) + k):
        a += word[len(word) - i]
    return a


if __name__ == "__main__":
    lines = get_lines_from_file("input.txt")

    lines = [' '.join(map(reverse_the_word_randomly, x.split())) for x in lines]

    put_lines_to_file("output.txt", lines)