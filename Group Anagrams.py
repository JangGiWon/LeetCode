import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            # 정렬해서 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)

        return anagrams.values()
