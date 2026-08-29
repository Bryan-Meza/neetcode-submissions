class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0

        n, m = len(word), len(abbr)

        while i < n and j < m:
            if abbr[j] == '0':
                break

            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isalpha():
                break
            else:
                sublen = 0
                while j < m and abbr[j].isdigit():
                    sublen = sublen * 10 + int(abbr[j])
                    j += 1
                i += sublen

        return i == n and j == m