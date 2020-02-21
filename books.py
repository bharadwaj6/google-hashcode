from collections import *

NO_BOOKS = 'no_books'
NO_DAYS = 'no_days'
SHIP_BOOKS = 'ship_books'
BOOK_IDS = 'book_ids'


class Solution:
    def order_books(self, input_file):
        with open('input/' + input_file) as f:
            lines = f.readlines()
            B, L, D = [int(x) for x in lines[0].split()]
            book_scores = [int(x) for x in lines[1].split()]
            libraries = defaultdict(dict)
            ctr = 2
            for l in range(L):
                libraries[l][NO_BOOKS], libraries[l][NO_DAYS], libraries[l][SHIP_BOOKS] = [int(x) for x in lines[ctr].split()]
                libraries[l][BOOK_IDS] = [int(x) for x in lines[ctr+1].split()]
                ctr += 2

            # approach 1 - simple one by one in given order
            res = []
            res.append(str(len(libraries)))
            for l, vals in libraries.items():
                bookids = vals[BOOK_IDS]
                res.append(' '.join([str(l), str(len(bookids))]))
                res.append(' '.join([str(x) for x in bookids]))
            with open('output/' + input_file.replace('in', 'out'), 'w') as f:
                f.write('\n'.join(res))

s = Solution()
for fname in ['a','b','c','d','e','f']:
    s.order_books(fname + '.in')
