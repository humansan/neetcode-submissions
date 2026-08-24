from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # sort the strings (could also create a count map for each one)
        # put strings into hashmap, where key is an anagram group (sorted string), and the values are indices of all the sorted strings that are equal to that sorted string
            # iterate through sorted strings, see if exists in map, if so then add index, else create key

        # iterate through map and create results list
        sorted_strs = [str(sorted(s)) for s in strs]

        anagrams_map = defaultdict(list)

        for index, sorted_str in enumerate(sorted_strs):
            anagrams_map[sorted_str].append(index)

        result = []
        
        for group in anagrams_map:
            this_group = []
            for index in anagrams_map[group]:
                this_group.append(strs[index])
            result.append(this_group)

        return result