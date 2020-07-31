import collections

strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

anagrams = collections.defaultdict(list)

for word in strs:
    # 정렬해서 딕셔너리에 추가
    anagrams[''.join(sorted(word))].append(word)
    # print(anagrams)

print(anagrams.values())
