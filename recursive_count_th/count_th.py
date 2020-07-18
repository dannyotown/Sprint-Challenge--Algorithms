'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

cache = {'count': 0}


def count_th(word):
    if len(word) < 2:
        val = cache['count']
        cache['count'] = 0
        return val
    elif (word[-2:]) == 'th':
        cache['count'] += 1
    return count_th(word[:-1])


print(count_th('abcthefthghith'))
