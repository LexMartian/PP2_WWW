def has_007(nums):
    for i in range(0, len(nums) - 2):
        if nums[i] == nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False
        
input_string = input('Enter elements of a list separated by space \n')
user_list = input_string.split()

# convert each item to int type
for i in range(len(user_list)):
    user_list[i] = int(user_list[i])
    

if has_007(user_list) == True:
    print("True")
else:
    print("False")