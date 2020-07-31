class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []

        # split()으로 나눠서 1번째 인덱스가 숫자인지 여부를 확인 후 리스트에 저장
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # 2개의 키를 람다 표현식으로 정렬
        # 첫 번째는 1번 인덱스이후 두 번째는 0번 인덱스
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letters + digits
