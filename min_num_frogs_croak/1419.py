class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c = r = o = a = k = ans = cur = 0
        # need to know, at particular point,
        # what are the max frog are croaking,

        for i, v in enumerate(croakOfFrogs):
            if v == 'c':
                c += 1
				# c gives a signal for a frog
                cur += 1
            elif v == 'r':
                r += 1
            elif v == 'o':
                o += 1
            elif v == 'a':
                a += 1
            else:
                k += 1
				# frog stop croaking
                cur -= 1

            ans = max(ans, cur)
            # if any inoder occurs;
            if c < r or r < o or o < a or a < k:
                return -1

        # if all good, else -1
        if cur == 0 and c == r and r == o and o == a and a == k:
            return ans
        return -1

