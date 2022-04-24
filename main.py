from __future__ import unicode_literals
from hazm import *
import tqdm
import random
import numpy as np
import nltk
import pandas as pd
import codecs


def main():
    file = open("input.txt", "r", encoding='utf-8')
    file_contents = file.read()

    normalizer = Normalizer()
    normalized = normalizer.normalize(file_contents)
    sentences = sent_tokenize(normalized)
    # for sentence in sentences:
    #     if sentence.startswith('مواد لازم'):
    #







if __name__ == '__main__':
    main()
