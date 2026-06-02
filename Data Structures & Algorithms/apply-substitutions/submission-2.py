class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        did_change = True
        while did_change:
            did_change = False
            for _from, _to in replacements:
                split = text.split('%' + _from + '%')
                if len(split) > 1:
                    did_change = True
                text = _to.join(split)
        return text
        