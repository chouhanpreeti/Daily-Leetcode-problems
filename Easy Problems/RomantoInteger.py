def romanToInt(s):
    '''Takes in a Roman representation of number to return in Nimerical format'''

    #storing the roman representation in a dictionary 
    roman_vals = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D': 500, 'M': 1000}
    #storing the last (right most) value in the variable which will be added and updated from right to left 
    answer = roman_vals[s[len(s)-1]]

    #loop from 2nd last roman value from right to left most value
    for index in range(len(s)-2, -1, -1):
        #storing the value into a temp variable
        val = roman_vals[s[index]]

        #checking condition
        #if the current value is smaller than the right most value we ave already encountered
        if roman_vals[s[index]] < roman_vals[s[index+1]]:
            #subtract the current value from the updated variable with answer
            answer -= val
        # if the current value fi larger than the right most value we have already encountered
        else:
            #then add the value to the variable and update it 
            answer += val

    return answer 
            


print(romanToInt("LVIII"))