# Find the longest panlindromic substring
# What the heck is a panlindromic substring? 
# - a substring that is the same forwards as it is backwards
# - bab == bab
# Edge cases?
# - What if there are two substring the same length? - return one
# - What if there is only one char? - return 1 char
# - What if there is no string? - return ""

# Brute force solution
# Check every permutaiton of the the string, and that is O(n^3)

# What if we try a strategy where we expand from the middle to the left or the right? 
# edge case here is string of odd length

class Solution:

    def longest_palindrome(self, s: str) -> str:
        def expand_around_center(string: str, start_index: int, end_index:int) -> str:
            start_pointer, end_pointer = start_index, start_index
            while start_index >= 0 and end_index < len(string) and  string[start_index] == string[end_index]:
                if end_index - start_index > end_pointer - start_pointer:
                    start_pointer, end_pointer = start_index, end_index
                start_index -= 1
                end_index += 1
            return string[start_pointer:end_pointer+1]  # include char at hi

        word_list = []
        length = len(s)
        for i in range(length):
            word_list.append(expand_around_center(s, i, i))
            word_list.append(expand_around_center(s, i, i + 1))
        return max(word_list, key=lambda s: len(s))


if __name__ == "__main__":
    s = Solution()
    print(s.longest_palindrome("twbiqwtafgjbtolwprpdnymaatlbuacrmzzwhkpvuwdtyfjsbsqxrlxxtqkjlpkvpxmlajdmnyepsmczmmfdtjfbyybotpoebilayqzvqztqgddpcgpelwmriwmoeeilpetbxoyktizwcqeeivzgxacuotnlzutdowiudwuqnghjgoeyojikjhlmcsrctvnahnoapmkcrqmwixpbtirkasbyajenknuccojooxfwdeflmxoueasvuovcayisflogtpxtbvcxfmydjupwihnxlpuxxcclbhvutvvshcaikuedhyuksbwwjsnssizoedjkbybwndxpkwcdxaexagazztuiuxphxcedqstahmevkwlayktrubjypzpaiwexkwbxcrqhkpqevhxbyipkmlqmmmogrnexsztsbkvebjgybrolttvnidnntpgvsawgaobycfaaviljsvyuaanguhohsepbthgjyqkicyaxkytshqmtxhilcjxdpcbmvnpippdrpggyohwyswuydyrhczlxyyzregpvxyfwpzvmjuukswcgpenygmnfwdlryobeginxwqjhxtmbpnccwdaylhvtkgjpeyydkxcqarkwvrmwbxeetmhyoudfuuwxcviabkqyhrvxbjmqcqgjjepmalyppymatylhdrazxytixtwwqqqlrcusxyxzymrnryyernrxbgrphsioxrxhmxwzsytmhnosnrpwtphaunprdtbpwapgjjqcnykgspjsxslxztfsuflijbeebwyyowjzpsbjcdabxmxhtweppffglvhfloprfavduzbgkw"))

