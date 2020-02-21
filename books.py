from collections import *

NO_BOOKS = 'no_books'
NO_DAYS = 'no_days'
SHIP_BOOKS = 'ship_books'
BOOK_IDS = 'book_ids'


class Solution:
    def __init__(self, input_file):
        self.input_file = input_file
        self.output_file = 'output/' + self.input_file.replace('in', 'out')
        with open('input/' + self.input_file) as f:
            lines = f.readlines()
            self.B, self.L, self.D = [int(x) for x in lines[0].split()]
            self.book_scores = [int(x) for x in lines[1].split()]
            self.libraries = defaultdict(dict)
            ctr = 2
            for l in range(self.L):
                self.libraries[l][NO_BOOKS], self.libraries[l][NO_DAYS], self.libraries[l][SHIP_BOOKS] = [int(x) for x in lines[ctr].split()]
                self.libraries[l][BOOK_IDS] = [int(x) for x in lines[ctr+1].split()]
                ctr += 2
    
    def order_books(self):
        # approach 1 - simple one by one in given order
        return self.libraries

    def get_schedule(self, ):
        out_libaries = self.order_books()
        
        res = [str(len(out_libaries))]
        for l, vals in out_libaries.items():
            bookids = vals[BOOK_IDS]
            res.append(' '.join([str(l), str(len(bookids))]))
            res.append(' '.join([str(x) for x in bookids]))
        
        with open(self.output_file, 'w') as f:
            f.write('\n'.join(res))


for fname in ['a','b','c','d','e','f']:
    s = Solution(fname + '.in')
    s.get_schedule()
