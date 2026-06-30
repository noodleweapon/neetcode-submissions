class Solution:
    def expand(self, s: str) -> List[str]:
        # k{a,zzz{b,c}}
        # "a, zzzb, zzzc"
        # [['k'], [['a'], ['z', 'z', 'z', [['b'], ['c']]]]]

        arr = []
        ptr_stack = [arr]
        word = ''
        for i in range(len(s)):
            if s[i] in list('{},') and word:
                ptr_stack[-1].append(word)
                word = ''
            if s[i] == '{':
                arr.append([])
                ptr_stack.append(arr[-1])
            elif s[i] == '}':
                ptr_stack.pop()
            elif s[i] == ',':
                pass
            else:
                word += s[i]
        if word != '':
            ptr_stack[-1].append(word)

        def dfs(items):
            res = ['']
            for item in items:
                if isinstance(item, str):
                    new_res = []
                    for prefix in res:
                        new_res.append(prefix + item)
                    res = new_res
                else:
                    options = []
                    for option in item:
                        options += dfs(option)
                    new_res = []
                    for prefix in res:
                        for option in options:
                            new_res.append(prefix + option)
                    res = new_res
            return res
        res = dfs(arr)
        res.sort()
        return res