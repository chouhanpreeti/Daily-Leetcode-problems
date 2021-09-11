def twoSum(nums, target):
    answer = []
        
    for indx, number_1 in enumerate(nums):
        number_2= target - number_1
            
        if number_2 in nums and indx!=nums.index(number_2):
            answer.append(indx)
            answer.append(nums.index(number_2))
            break
        else:
            continue 
        
    return answer 

