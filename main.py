from __future__ import unicode_literals
from hazm import *
import tqdm
import random
import numpy as np
import nltk
import pandas as pd
import codecs

def find_word(list, word):
    for i in range(len(list)):
        if list[i][0].startswith(word):
            return i



def main():
    file = open("input.txt", "r", encoding='utf-8')
    file_contents = file.read()

    normalizer = Normalizer()
    normalized = normalizer.normalize(file_contents)
    sentences = sent_tokenize(normalized)
    sentencess = []
    for sentence in sentences:
        sentencess.append(sentence.split('\n'))


    i = find_word(sentencess, 'مواد لازم')
    j = find_word(sentencess[i:], 'طرز تهیه')
    # for t in range(i+1, j):
    #     sentencess[t].find
    # print(sentencess[i+1:j])
    # print(*sentencess[j+1:])
    separators = [normalizer.normalize(x.strip()) for x in codecs.open('separators.txt', 'r', 'utf-8').readlines()]
    print(separators)
    num = ['۱', '۲', '۳','۴','۵','۶','۷','۸','۹']
    for t in range(i+1, j):

        z = len(sentencess[t][0])
        if sentencess[t][0][0] in num:
            sentencess[t][0]= sentencess[t][0].split(maxsplit=1)[1]
        # if sentencess[t][0].startswith():

        # z = 0
        for separator in separators:
            curr_index = sentencess[t][0].find(separator)
            # z = max(z, curr_index)

            if curr_index != -1 and curr_index < z:
                z = curr_index



        print(sentencess[t][0][:z])
        print(sentencess[t][0][z:])



    # for sentence in sentences:
    #     if sentence.startswith('مواد لازم'):






if __name__ == '__main__':
    main()
