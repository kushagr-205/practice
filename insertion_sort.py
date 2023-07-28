nums = list()

entries = str(input("Enter the numbers to be sorted: "))
num = entries.split(",")
nums = [int(i) for i in num]

print(nums)
n = len(nums)

def swap(j):
    temp = nums[j]
    nums[j] = nums[j + 1]
    nums[j + 1] = temp

def insert_sort(nums, n):
    for i in range(0, n-1):
        for j in range (i, n-1):
            while j>=0:
                if nums[j] > nums[j+1]:
                    swap(j)
                    j -= 1
                else:
                    break
            break

insert_sort(nums, n)
print(nums)