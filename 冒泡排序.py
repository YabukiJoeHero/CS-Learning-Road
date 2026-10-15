#吐槽：本是大一上学期就该搞明白的基础，现在才亡羊补牢
#也叫 “沉底排序”

#第一步：两个数的交换
# a = 10
# b = 15
# a,b = b,a
# print(a,b)

nums = [30,12,56,9,8,68,2]  #6次
# for j in range(0,len(nums)-1):
#     if nums[j] > nums[j+1]:
#         nums[j],nums[j+1] = nums[j+1],nums[j]
# print(nums)

def bubble(nums):
    for i in range(len(nums)-1):
        for j in range(0,len(nums)-1-i): #减少单个循环中的比较次数
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
        print(nums)

bubble(nums)