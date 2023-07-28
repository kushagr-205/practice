nums = list()

entries = str(input("Enter the numbers to be sorted: "))
num = entries.split(",")
nums = [int(i) for i in num]

print(nums)
n = len(nums)

def swap(i, ind, temp):
    nums[ind] = nums[i]
    nums[i] = temp

def select_sort(nums, n):
    for i in range(0, n-1):
        temp = nums[i]
        for j in range(i, n-1):
            if nums[j+1] < temp:
                temp = nums[j+1]
                ind = j+1
        if temp != nums[i]:
            swap(i, ind, temp)

select_sort(nums, n)
print(nums)