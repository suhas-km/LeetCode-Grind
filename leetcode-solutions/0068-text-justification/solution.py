class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16

        res = []
        line, length = [], 0
        i = 0

        while i < len(words):
            # line complete?
            if length + len(line) + len(words[i]) > maxWidth: # if length of current line + empty spaces + len of current word > maxWidth
                extra_space = maxWidth - length
                spaces = extra_space // max(1, len(line) - 1) # max because it helps avoid divide by 0 case
                remainder = extra_space % max(1, len(line) - 1)

                for j in range(len(line) - 1): # executes atleast 1 time and handles the case of the only word in the line
                    line[j] += " " * spaces
                    if remainder:
                        line[j] += " " # adding space to the end
                        remainder -= 1

                # fix: handle single-word non-last line
                if len(line) == 1:
                    line[0] += " " * extra_space

                res.append("".join(line))
                line, length = [], 0 # reset line and length

            line.append(words[i])
            length += len(words[i])
            i += 1
        
        # Handling the last line
        last_line = " ".join(line)
        trailing_space = maxWidth - len(last_line)
        res.append(last_line + " " * trailing_space)

        return res

