import copy
import random
from collections import defaultdict

RANDOM_TIMES = 200000


class Solution:
    def get_best(self, sizes):
        mapping = copy.deepcopy(self.mapping)
        new_sizes = copy.deepcopy(sizes)
        random.shuffle(new_sizes)

        total, added = 0, []
        for size in new_sizes:
            if total + size <= M:
                idx = mapping[size].pop()
                added.append(idx)
                total += size
        del mapping
        del new_sizes
        return total, added[::-1]

    def normal_best(self):
        best1, idxs1 = self.get_best(sizes)
        best2, idxs2 = self.get_best(sizes[::-1])
        return (best1, idxs1) if best1 > best2 else (best2, idxs2)

    def get_best_greedy(self, sizes):
        self.mapping = defaultdict(list)
        for i, s in enumerate(sizes):
            self.mapping[s].append(i)

        # randomized algorithm, shuffle and iterate for 10 iterations
        best, ret = self.normal_best()
        for k in range(RANDOM_TIMES):
            if k % 100 == 0:
                print('shuffling: ', k)
            res, idxs = self.get_best(sizes)
            if res > best:
                print('found better score: ', res)
                best = res
                ret = idxs
        return ret

    def get_pizzas(self, M, N, sizes):
        if M > 100000:
            return self.get_best_greedy(sizes)

        dp = [[0] * (M + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if sizes[i - 1] <= j:
                    dp[i][j] = max(sizes[i - 1] + dp[i - 1][j - sizes[i - 1]], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]

        res = dp[N][M]
        m = M
        output = []
        for i in range(N, 0, -1):
            if res <= 0:
                break
            if res == dp[i - 1][m]:
                continue
            else:
                output.append(i - 1)
                res -= sizes[i - 1]
                m -= sizes[i - 1]
        return output[::-1]


s = Solution()
print(s.get_pizzas(17, 4, [2, 5, 6, 8]))

filenames = ['a_example.in', 'b_small.in', 'c_medium.in', 'd_quite_big.in', 'e_also_big.in']
outputs = ['a.output', 'b.output', 'c.output', 'd.output', 'e.output']
input_prefix = './input/'
output_prefix = './output/'

for idx, filename in enumerate(filenames):
    print('running for file {}'.format(idx))

    with open(input_prefix + filename, 'r') as file:
        lines = file.readlines()

    M, N = [int(x) for x in lines[0].split()]
    sizes = [int(x) for x in lines[1].split()]

    s = Solution()
    out = s.get_pizzas(M, N, sizes)
    out_lines = [str(len(out))]
    out_lines.append(' '.join([str(x) for x in out]))
    final = '\n'.join(out_lines)
    with open(output_prefix + outputs[idx], 'w') as output_file:
        output_file.write(final)
