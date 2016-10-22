class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def helper(s, count, tmp, results):
            if count == 4:
                # This condition prevents us from adding truncated result
                # e.g., '11111111111111111111111111111111111111111111'
                if len(s) == 0:
                    results += tmp[:-1],
                return

            for i in range(1, 4):
                # This condition prevents us from adding duplicated result
                # e.g., '0000' will result in ["0.0.0.0","0.0.0.0","0.0.0.0"]
                if len(s) < i:
                    continue
                current = s[:i]
                num = int(current)
                if num > 255 or str(num) != current:
                    continue
                helper(s[i:], count+1, tmp+current+'.', results)

        results = []
        helper(s, 0, '', results)
        return results