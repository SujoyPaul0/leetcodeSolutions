'''
Example 1:

Input: num = 3749

Output: "MMMDCCXLIX"

Explanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
'''
class Solution:
    def intToRoman(self, num: int) -> str:
        hmap = {
                1:    'I',
                4:    'IV',
                5:    'V',
                9:    'IX',
                10:    'X',
                40:    'XL',
                50:    'L',
                90:    'XC',
                100:    'C',
                400:    'CD',
                500:    'D',
                900:    'CM',
                1000:    'M'
                            }

        r = ''
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            while n <= num:
                r += hmap[n]
                num -= n
        
        return r