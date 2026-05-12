class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        lengths = []
        for word in words:
            l = len(word)
            if (not lines) or (lengths[-1] + 1 + l > maxWidth):
                # first word on line
                lines.append([word])
                lengths.append(l)
            else:
                # second word on line.
                lines[-1].append(word)
                lengths[-1] += 1 + l
            
        n = len(lines)

        res = []
        for r, line in enumerate(lines):
            slots = len(line) - 1
            if slots == 0 or r == len(lines) - 1:
                text = " ".join(line)
                text += " " * (maxWidth - lengths[r])
                res.append(text)
                continue

            spaces = maxWidth - (lengths[r] - slots)
            min_pads = spaces // slots
            extra_pads = spaces - slots * min_pads
            
            text = ""
            for c, word in enumerate(line):
                text += word
                if c == len(line) - 1:
                    break
                text += " " * min_pads
                if extra_pads > 0:
                    extra_pads -= 1
                    text += " "
            res.append(text)
        
        return res
        
