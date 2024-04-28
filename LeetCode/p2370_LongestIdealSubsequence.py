# You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following conditions are satisfied:
#     t is a subsequence of the string s.
#     The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.
# Return the length of the longest ideal string

# class Solution(object):
#     alphabet = "abcdefghijklmnopqrstuvwxyz" # can achieve O(1) access if in dict form
#     tree = None
#     def __init__(self):
#         self.tree = dict()

#     def longestIdealString_(self, s, i, k):
#         if self.tree.get(i, None) != None:
#             return self.tree[i]
#         if i >= len(s):
#             return 0
#         elif i + 1 >= len(s):
#             self.tree[i] = 1
#             return 1
        
#         values = []
#         for index, letter in enumerate(s[i+1:]):
#             if abs(self.alphabet.index(s[i]) - self.alphabet.index(letter)) <= k:
#                 values.append(self.longestIdealString_(s, index+i+1, k))
#         if len(values) <= 0:
#             self.tree[i] = 1
#             return 1
#         self.tree[i] = 1 + max(values)
#         return self.tree[i]

#     def longestIdealString(self, s, k):
#         maxV = 0
#         for i in range(len(s)):
#             tmp = self.longestIdealString_(s, i, k)
#             if tmp > maxV:
#                 maxV = tmp
#         return maxV
### ~O(n!) time, O(n) space

# class Solution(object):
#     alphabet = "abcdefghijklmnopqrstuvwxyz" # can achieve O(1) access if in dict form
#     tree = None
#     def __init__(self):
#         self.tree = dict()

#     def longestIdealString(self, s, k):
#         totalMax = 0
#         for i, letter in enumerate(s):
#             maxLength = 0
#             maxLetter = None
#             for j in range(0,i):
#                 if self.tree.get(j, None) != None:
#                     length, lastL = self.tree[j]
#                     if abs(self.alphabet.index(lastL) - self.alphabet.index(letter)) <= k:
#                         if length > maxLength:
#                             maxLength = length
#                             maxLetter = lastL
#             if 1 + maxLength > totalMax:
#                 totalMax = 1 + maxLength
#             self.tree[i] = (1 + maxLength, letter)
#         return totalMax
### O(n^2) time, O(n) space

class Solution(object):
    alphabet = "abcdefghijklmnopqrstuvwxyz" # can achieve O(1) access if in dict form
    tree = None
    def __init__(self):
        self.tree = [0 for i in range(26)]

    def longestIdealString(self, s, k):
        for letter in s:
            i = self.alphabet.index(letter)
            for j in range(max(0, i-k), min(25, i+k)+1):
                self.tree[i] = max(self.tree[i], self.tree[j])
            self.tree[i] += 1
        return max(self.tree) 
### O(n) time, O(1) space
    
if __name__ == "__main__":
    print(Solution().longestIdealString("acfgbd", 2)) # 4
    print(Solution().longestIdealString("ebcd", 3)) # 4
    print(Solution().longestIdealString("eduktdb", 15)) # 5
    print(Solution().longestIdealString("pvjcci", 4)) # 2
    print(Solution().longestIdealString("dyyonfvzsretqxucmavxegvlnnjubqnwrhwikmnnrpzdovjxqdsatwzpdjdsneyqvtvorlwbkb", 7)) # 42
    print(Solution().longestIdealString("fqyokqgzvjpermqmwcjqtzbxnurjmawsswlwzmnjbbhdtfjxnktwtonpeorewc", 3)) # 19
    print(Solution().longestIdealString("gdzfefmwfqlsdskuvbwtykjrheothigkfuxdrjjitiopxbajqtxnagqxuqtupmogdgqimiltbosujabgieewpxwbhomumgrpwhfxmhwpnuwtdrkktxwuwkfqtcgrptqvtdgsvtcyephhnpkvcosjqlyvlhbgpnllseckuulebtzrpjxhdjsrwxqeksschqzncecguwjvwwjqztphyfcfivzmerezgixhqrmrfivxyjrigzzinevawpfetxdxsdwuakljswyicevpznqieyalushpztmvoolduqqxytgywzfqdjaakdpstkfflzdtjdwzhnssykrrnkqeabhgdgdhtlxvnzphaoggkymqkcvaspoctckktnhjggtlndlnpmupgnnifazvukhgcvxfsbrojsebanxtraizewoulierxejktvuzdcxbzcextncrbmgwsjafcoerwnwqxltqbdleihcrodhzpxxexwocmyqxunzfliwzgqmnhwljvvnipxruanelhqsspajdqtqwfhuilvxfwfodkpevrvxoonybahhqebkltsfvltarmdulrwwmmlfjdjjimqdxhmgwpgxtpdpluizntitgxktklcjnhmidtwbejwvwaxfvnxbwyeokvklyiqaopbtrihroelrbhgzamvdeuhtsbeqivcuexltdcxkwbeycrvhmnueritvabjgskiayazfstegslkdhhuhznuzmcaokddpdwzpmrqqzvxgqprojuqedthdsoxtgometwrmkcsnbnlhwijbzhgkqrjpbivfvdafbcovomiukqriwfwdblefmvhlojreljtwihxcpbrxecgjjdkpqeljvvrekdcygnmpukmikantrfkqtrlnfettvjaybjhookrgufwfsssvzckcggjnpnciyemxnwteihjkbtcdbyvwnurjtwlunddmitbjhbnwpddjpreoocyhdsboctmpaubipxqfykuzchrzyfmilhfgrlwzshsdbqmidoidbhrtaefdeghsxgcdzgyvtfojnntxmovtkyhstlligxpvcqrwkwjimyubaovvafkdlaqfudusgewfryytcjsjetmjxyaudxnmzmcawlfnjehrduvckwyqigrikzhabqesyqxvlgnvfppsencdsujrmgkbweqzkymzyourjyeyzglalkbotuosilmtigxombmplnoequxyhyocjkynlmqbetoplxhfgqbocfifvkojqtvlovlelddwjkambjotvzrmzmygxevvfqqguaqisphzsxckrvpwfilkvyshyuykfvtsgzpkjnlbhouesnlzztrxurmqzxiqlptdyebcarqjlgqvgesjaeerjjlamuppzogsxmldspuzeqizosaocfgxtunnnamqdsazfsiiuqlynmfxxhu", 15)) # 1247