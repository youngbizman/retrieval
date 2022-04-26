from __future__ import unicode_literals
from hazm import *
import codecs
import timeit
import re


def find_word(list, word):
    '''for finding ingredients.txt string'''
    result = []
    for i in range(len(list)):
        if list[i].find(word) != -1 and len(list[i]) < 40:
            result.append(i)
    return result


def find_word2(list, word):
    '''for finding recipe string'''
    result = []
    for i in range(len(list)):
        if list[i].startswith(word):
            # list[i].replace(word, "")
            result.append(i)
    return result


def find_next(list, m):
    try:
        return next(val for val in list if val > m)
    except StopIteration:
        return None


def set_default(sentencess):
    ''' find the first line with more than 40 characters '''

    i = 0
    while len(sentencess[i]) < 40:
        i += 1
    if i == len(sentencess):
        return []
    else:
        return i

# def is_char(c):
#     'check a charecter is persion or not'
#     if c in 'اآبپتسجچهخدذرزسشصضطظعغفقکلمنوهیي':
#         return True
#     return False


def main():
    file = open("input.txt", "r", encoding='utf-8')
    file_contents = file.read()

    sentencess = file_contents.split('\n')
    # "to remove empty lines"
    # sentencess = list(filter(None, sentencess))
    file.close()

    result = {"ingredients": [], "quantity": [], "recipie": [], "span_ingredients": [], "span_recipie": []}
    start = timeit.default_timer()

    normalizer = Normalizer()

    separators = [normalizer.normalize(x.strip()) for x in codecs.open('separators.txt', 'r', 'utf-8').readlines()]
    preparators = [normalizer.normalize(x.strip()) for x in codecs.open('preparation.txt', 'r', 'utf-8').readlines()]
    ingredient_start = [normalizer.normalize(x.strip()) for x in codecs.open('ingredients.txt', 'r', 'utf-8').readlines()]

    '''مواد لازم  از ایندکس چندم شروع می شن '''
    l1 = []
    for i in ingredient_start:
        l1 += find_word2(sentencess, i)

    '''طرز تهیه ها از ایندکس چندم شروع می شن '''
    l2 = []
    for preparator in preparators:
        l2 += find_word2(sentencess, preparator)

    if len(l2) == 0:
        '''حالت پیش فرض'''
        l2.append(set_default(sentencess))

    l3 = l1 + l2
    l3.sort()
    for i in l2:
        next = find_next(l3, i)

        if len(sentencess[i]) < 40:
            i = i+1
        else:
            sentencess[i] = re.sub(r'^.+:', '', sentencess[i])
        print('jnsk',sentencess[i])
        recipe = "\n".join(sentencess[i: next])
        loc = file_contents.index(recipe)
        result["span_recipie"].append([loc, loc + len(recipe)])

        result["recipie"].append(recipe.replace("\n", ""))

    num = ['۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹']
    print(l1, l2, l3)
    for j in l1:
        next = find_next(l3, j)
        print(j, next)

        for t in range(j + 1, next):

            z = len(sentencess[t])
            if z == 0:
                continue

            if sentencess[t] in num:
                sentencess[t] = sentencess[t].split(maxsplit=1)[1]

            for separator in separators:
                curr_index = sentencess[t].find(separator)
                '''اگر اشتباهی مچ کرده بود(مثلا دو در دوغ رو)'''
                # if is_char(sentencess[t][curr_index-1]) or is_char(sentencess[t][curr_index+1]):
                if sentencess[t][curr_index-1] != ' ' and sentencess[t][curr_index+1] != ' ':
                    continue

                if curr_index != -1 and curr_index < z:
                    z = curr_index

            loc = file_contents.index(sentencess[t])
            result["span_ingredients"].append([loc, loc + len(sentencess[t])])

            result["ingredients"].append(re.sub(r'^[\W_]+|[\W_]+$', '', sentencess[t][:z]))
            result["quantity"].append(sentencess[t][z:])

    stop = timeit.default_timer()
    result["time"] = stop - start
    print(result)


if __name__ == '__main__':
    main()
