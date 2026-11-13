class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False
        
        seen_brackets = []

        for bracket in s:
            if bracket in [")", "}", "]"]:
                if seen_brackets:
                    if bracket == ")" and seen_brackets.pop(-1) == "(":
                        continue
                    elif bracket == "}" and seen_brackets.pop(-1) == "{":
                        continue
                    elif bracket == "]" and seen_brackets.pop(-1) == "[":
                        continue
                    else:
                        return False
                else:
                    return False
            elif bracket in ["(", "{", "["]:
                seen_brackets.append(bracket)
            elif len(seen_brackets) == 0:
                return False
            else:
                return False
        if len(seen_brackets) != 0:
            return False
        return True

        