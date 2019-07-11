#!/usr/bin/env python3
import random
import sys

number_of_lines = 5

if len(sys.argv) > 1:
    input_line = sys.argv[1]
    try:
        n = int(input_line)
        if 1 <= n <= 10:
            number_of_lines = n
        else:
            print('lines must be 1-10 inclusive')
    except ValueError as err:
        print(f'error : {err}')

articles = ("the", "a")
subjects = ('cat', 'dog', 'man', 'woman')
verbs = ('sang', 'ran', 'jumped')
adverbs = ('loudly', 'quietly', 'well', 'badly')
structures = ((articles, subjects, verbs, adverbs), (articles, subjects, verbs))

for i in range(number_of_lines):
    variant = random.randint(0, 1)
    new_line = ''
    for list_of_words in structures[variant]:
        new_line += ' ' + random.choice(list_of_words)
    print(new_line)
