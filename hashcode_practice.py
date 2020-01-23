from collections import defaultdict


class Solution:
    def get_best_greedy(self, M, N, sizes):
        mapping = defaultdict(list)
        for i, s in enumerate(sizes):
            mapping[s].append(i)
        
        sizes = sorted(sizes)
        total = 0
        added = []
        for size in sizes[::-1]:
            if total + size <= M:
                idx = mapping[size].pop()
                added.append(idx)
                total += size
        return added[::-1]
    
    def get_pizzas(self, M, N, sizes):
        if M > 100000:
            return self.get_best_greedy(M, N, sizes)
        
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
