# 버블정렬🧼
서로 인접한 두 원소를 비교하여 교환하며 정렬하는 방법. 교환하는 모습이 보글보글 거품같다고 하여 버블정렬이다.

### 정렬방식
![](https://velog.velcdn.com/images/jpdev/post/5ce53e6b-c1cb-4123-939e-5f8f8807b9fb/image.gif)


1. 범위를 설정해준다.
2. 두 원소를 앞에서부터 비교해나가며 앞의 원소가 더 크면 뒤의 원소와 swap 한다.
3. swap하며 나아가다 한 사이클(모든 범위)을 다 돌았으면 범위를 뒤에서부터 한칸씩 줄인다.
4. 범위가 0이 될때까지 반복

```python
for i in range(n - 1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
```
**_궁금증 : 앞에서부터 정렬해나가면 안되나?에 대한 코드_**
```python
import copy, random

n = 5
nums = [i for i in range(1, n+1)]
random.shuffle(nums)
arr = copy.deepcopy(nums)
swap = 0

#버블정렬
print(nums)
bubbleSwap = 0
for i in range(n):
    for j in range(i+1, n):
      if nums[i] > nums[j]:
          nums[i], nums[j] = nums[j], nums[i]
          bubbleSwap += 1
print(nums, bubbleSwap)

arrSwap = 0
for i in range(n - 1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            arrSwap += 1
print(arr, arrSwap)

# [4, 2, 1, 5, 3]
# [1, 2, 3, 4, 5] 5
# [1, 2, 3, 4, 5] 5
```


### 시간복잡도
O(n^2)
### 특징
**장점**
- 구현이 쉽다.

**단점**
- 시간복잡도가 높아 효율성이 떨어진다.
- 특정 요소가 최종 위치에 있더라도 교환이 일어날 수 있음(효율성 문제)
