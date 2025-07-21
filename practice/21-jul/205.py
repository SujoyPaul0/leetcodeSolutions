class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}

        for ch_s, ch_t in zip(s, t):
            if ch_s in s_map and s_map[ch_s] != ch_t:
                return False
            if ch_t in t_map and t_map[ch_t] != ch_s:
                return False
            s_map[ch_s] = ch_t
            t_map[ch_t] = ch_s
        
        return True