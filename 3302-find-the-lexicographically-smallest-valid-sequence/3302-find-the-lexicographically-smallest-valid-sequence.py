class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n = len(word1)
        m = len(word2)

        # suf[j] = earliest position where word2[j:]
        # can be matched exactly.
        suf = [-1] * (m + 1)
        suf[m] = n

        p = n - 1

        for j in range(m - 1, -1, -1):
            while p >= 0 and word1[p] != word2[j]:
                p -= 1

            if p < 0:
                break

            suf[j] = p
            p -= 1

        ans = []
        pos = 0
        used = False

        for j in range(m):
            while pos < n:

                # Option 1: use this position as a mismatch.
                if not used and word1[pos] != word2[j]:
                    if j == m - 1 or (
                        suf[j + 1] != -1 and suf[j + 1] > pos
                    ):
                        ans.append(pos)
                        pos += 1
                        used = True
                        break

                # Option 2: exact match.
                if word1[pos] == word2[j]:
                    ans.append(pos)
                    pos += 1
                    break

                pos += 1

            else:
                return []

        return ans