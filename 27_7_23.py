nums = [16, 21, 13, 24]

def square(n):
    return n**2

result = map(square, nums)
print(list(result))

res_2 = list(map(lambda x: x**2, nums))
print(res_2)

nums.sort(key=square, reverse=True)
print(nums)

nums.sort(key=lambda x: x**2)
print(nums)

marks = [("john", 88), ("Harry", 74), ("Rick", 93)]
marks.sort(key= lambda x: x[1])
print(marks)

hello = [15, 2, 23, 86, 9, 44]

def is_even(n):
    if n%2==0:
        return n

print(list(filter(is_even, hello)))

print(list(filter(lambda x: x%2==0, hello)))
