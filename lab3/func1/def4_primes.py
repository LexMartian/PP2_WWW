def filter_prime(nums):
    for i in nums:
        isPrime = True
        for j in range(2, i):
            if i % j == 0:
                isPrime = False
                break
        if isPrime and i > 1:
            print(i, end=" ")

input_string = input('Enter elements of a list separated by space \n')
user_list = input_string.split()

# convert each item to int type
for i in range(len(user_list)):
    user_list[i] = int(user_list[i])

filter_prime(user_list)