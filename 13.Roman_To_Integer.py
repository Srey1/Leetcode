def romanToInt(self, s: str) -> int:
    # Hashmap storing the conversions
    conversion = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
    num = 0
    i = 0
    # While this variable i is less than the length of the string
    while i < len(s):
        # If we are at the last letter or the current letter is greater than the next one then just add the value of the number to our result
        if (i == len(s)-1) or (conversion[s[i]] >= conversion[s[i+1]]):
            num += conversion[s[i]]
            i += 1
        # Otherwise add the difference between the next number and the current one. Ensure to add 2 to i so we skip the next letter too as we already added the difference
        else:
            num += conversion[s[i+1]]-conversion[s[i]]
            i += 2
    return num

        