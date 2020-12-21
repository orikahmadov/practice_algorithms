#Finding first and second min

def second_min(list): 
    f1,f2 = list[0], list[1]
    for i in range((len(nums))):
        if f1 > nums[i]:
            f1 =  nums[i]
        if nums[i] > f1:
            f2 =  nums[i]
    print("First min:", f1, "Second min:", f2)
