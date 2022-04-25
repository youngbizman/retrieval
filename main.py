from __future__ import unicode_literals
from hazm import *
import tqdm
import random
import numpy as np
import nltk
import pandas as pd
import codecs

def find_word(list, word):
    result = []
    for i in range(len(list)):
        if list[i].startswith(word):
            result.append(i)
    return result


def find_next(list, m):
    try:
        first_value = next(val for val in list if val > m)
    except StopIteration:
        first_value = None
    return first_value


def main():
    file = open("input.txt", "r", encoding='utf-8')
    file_contents = file.read()
    sentencess = file_contents.split('\n')
    file.close()


    normalizer = Normalizer()
    separators = [normalizer.normalize(x.strip()) for x in codecs.open('separators.txt', 'r', 'utf-8').readlines()]
    preparators = [normalizer.normalize(x.strip()) for x in codecs.open('preparation.txt', 'r', 'utf-8').readlines()]

    l1 = find_word(sentencess, 'مواد لازم')
    l2 = []
    for preparator in preparators:
        l2 += find_word(sentencess, preparator)

    l3 = l1 + l2
    for i in l2:
        next = find_next(l3, i)
        print(sentencess[i: next])


    num = ['۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹']

    for j in l1:
        next = find_next(l3, j)
        # print(sentencess[j+1:next])

        for t in range(j+1, next):

            z = len(sentencess[t])
            if sentencess[t] in num:
                sentencess[t] = sentencess[t].split(maxsplit=1)[1]

            for separator in separators:
                curr_index = sentencess[t].find(separator)

                if curr_index != -1 and curr_index < z:
                    z = curr_index

            print(sentencess[t][:z])
            print(sentencess[t][z:])


if __name__ == '__main__':
    main()
