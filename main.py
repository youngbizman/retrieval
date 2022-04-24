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
    print(sentencess[i+1:j])
    print(*sentencess[j+1:])



    # for sentence in sentences:
    #     if sentence.startswith('مواد لازم'):






if __name__ == '__main__':
    main()
