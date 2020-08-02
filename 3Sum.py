'''
투 포인터를 활용한 문제 풀이

'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()  # 처음에 정렬

        for i in range(len(nums) - 2):
            # 중복 값 건너 뛰기
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    results.append((nums[i], nums[left], nums[right]))

                    # 옆에도 같은 값이 존재 할 수 있으므로 검사한다.
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # 코드 상  sum == 0 이면 left, right가 움직이지 않기 때문에 각각 한 칸씩 이동한다.
                    left += 1
                    right -= 1

        return results
