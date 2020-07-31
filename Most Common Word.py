import collections
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # paragraph의 단어가 아닌 문자는 공백으로 전환
        # banned에 있는 문자가 아니라면 소문자로 전환하고 단어 별로 리스트에 저장
        words = [word for word in re.sub(
            r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        counts = collections.Counter(words)

        # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
        return counts.most_common(1)[0][0]
