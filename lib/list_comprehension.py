#!/usr/bin/env python3

def return_evens(num_list):
    pass
    return [num for num in num_list if num % 2 == 0]

num_list = range(10)
result = return_evens( num_list)
print(result)


def make_exclamation(sentence_list):
    pass
    return[sentence + '!' for sentence in sentence_list]

sentence_list = [
    "I like computers",
    "I require coffee",
    "Live long and prosper",
]

result = make_exclamation(sentence_list)
print(result)