class Solution:
    def encode(self, strs: List[str]) -> str:
        res = str(len(strs))
        for s in strs:
            res += ',' + str(len(s))
        res += ',' + ''.join(strs)
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        comma_split = s.split(',')
        num_words = int(comma_split[0])
        lens = list(map(int, comma_split[1:num_words+1]))
        joined_string = ','.join(comma_split[num_words+1:])

        res = []
        start_ind = 0
        for i in range(len(lens)):
            res.append(joined_string[start_ind:start_ind+lens[i]])
            start_ind += lens[i]

        return res