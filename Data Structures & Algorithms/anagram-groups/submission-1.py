from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # sort the strings (could also create a count map for each one)
        # put strings into hashmap, where key is an anagram group (sorted string), and the values are indices of all the sorted strings that are equal to that sorted string
            # iterate through sorted strings, see if exists in map, if so then add index, else create key

        # iterate through map and create results list
        anagrams_map = defaultdict(list)

        for s in strs:
            sorted_str = str(sorted(s))
            anagrams_map[sorted_str].append(s)
        
        return list(anagrams_map.values())