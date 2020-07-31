class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []

        # 영문자, 숫자만 리스트에 저장
        # 대소문자를 구분하지 않으므로 소문자로 전환
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # 리스트의 첫 번째와 마지막을 비교
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True
