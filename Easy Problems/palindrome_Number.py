def isPalindrome(x):
    temp = x
    reverse_num = 0

    if x < 0:
        return False
    else:
        while x:
            dig = x%10
            reverse_num = (reverse_num*10) + dig
            x = x//10

    return reverse_num == temp


print(isPalindrome(-121))