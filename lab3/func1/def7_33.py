def has_33(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] == nums[i + 1] == 3:
            return True
    return False
        
input_string = input('Enter elements of a list separated by space \n')
user_list = input_string.split()

# convert each item to int type
for i in range(len(user_list)):
    user_list[i] = int(user_list[i])
    

if has_33(user_list) == True:
    print("True")
else:
    print("False")