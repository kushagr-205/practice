nums = list()

entries = str(input("Enter the numbers to be sorted: "))
num = entries.split(",")
nums = [int(i) for i in num]

print(nums)
n = len(nums)

def swap(x, y, i):
    temp = x
    nums[i] = nums[i + 1]
    nums[i + 1] = temp

def bubble_sort(nums, n):
    count = 0
    for i in range (0, n):
        for j in range(0, n-1):
            if nums[j] > nums[j+1]:
                count += 1
                swap(nums[j], nums[j+1], j)
        if count == 0:
            break;

bubble_sort(nums, n)
print(nums)