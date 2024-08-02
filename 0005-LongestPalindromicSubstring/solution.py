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

    def longest_palindrome2(self, s: str) -> str:
        def expand_around_center(string: str, left_index: int, right_index: int) -> str:
            # Pointers used to keep track of the longest substring
            left_pointer, right_pointer = left_index, left_index
            # Start index is greater than 0
            # End index is not at the end of the string
            # Left and right character must match
            while (
                left_index >= 0
                and right_index < len(string)
                and string[left_index] == string[right_index]
            ):
                # When the length the new substring is longer than the stored substring
                # update the stored substring pointers
                if right_index - left_index > right_pointer - left_pointer:
                    left_pointer, right_pointer = left_index, right_index
                left_index -= 1
                right_index += 1
            # Compose the substring (+1 so that we include char at index)
            return string[left_pointer : right_pointer + 1]

        word_list = []
        length = len(s)
        # For each index of the string, look to the left and to the right
        for i in range(length):
            # Odd string
            word_list.append(expand_around_center(s, i, i))
            # Even string
            word_list.append(expand_around_center(s, i, i + 1))
            print(word_list)
        # Key can be a lambda function
        return max(word_list, key=len)


if __name__ == "__main__":
    s = Solution()
    string = "twbiqwtafgjbtolwprpdnymaatlbuacrmzzwhkpvuwdtyfjsbsqxrlxxtqkjlpkvpxmlajdmnyepsmczmmfdtjfbyybotpoebilayqzvqztqgddpcgpelwmriwmoeeilpetbxoyktizwcqeeivzgxacuotnlzutdowiudwuqnghjgoeyojikjhlmcsrctvnahnoapmkcrqmwixpbtirkasbyajenknuccojooxfwdeflmxoueasvuovcayisflogtpxtbvcxfmydjupwihnxlpuxxcclbhvutvvshcaikuedhyuksbwwjsnssizoedjkbybwndxpkwcdxaexagazztuiuxphxcedqstahmevkwlayktrubjypzpaiwexkwbxcrqhkpqevhxbyipkmlqmmmogrnexsztsbkvebjgybrolttvnidnntpgvsawgaobycfaaviljsvyuaanguhohsepbthgjyqkicyaxkytshqmtxhilcjxdpcbmvnpippdrpggyohwyswuydyrhczlxyyzregpvxyfwpzvmjuukswcgpenygmnfwdlryobeginxwqjhxtmbpnccwdaylhvtkgjpeyydkxcqarkwvrmwbxeetmhyoudfuuwxcviabkqyhrvxbjmqcqgjjepmalyppymatylhdrazxytixtwwqqqlrcusxyxzymrnryyernrxbgrphsioxrxhmxwzsytmhnosnrpwtphaunprdtbpwapgjjqcnykgspjsxslxztfsuflijbeebwyyowjzpsbjcdabxmxhtweppffglvhfloprfavduzbgkw"
    string = "abbaxyzz"
    print(len(string))
    print(s.longest_palindrome(string))
