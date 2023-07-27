nums = list()

more_elements = 1
while more_elements == 1:
    element = int(input("Input element in the list: "))
    nums.append(element)
    more_elements = int(input("Are there any more elements?\nEnter 1 for Yes, 0 for No:  "))
    if more_elements == 0:
        break;

print(nums)
n = len(nums)

def swap(x, y, i):
    temp = x
    nums[i] = nums[i + 1]
    nums[i + 1] = temp

def insert_sort(nums, n):
    count = 0
    for i in range (0, n):
        for j in range(0, n-1):
            if nums[j] > nums[j+1]:
                count += 1
                swap(nums[j], nums[j+1], j)
        if count == 0:
            break;

insert_sort(nums, n)
print(nums)