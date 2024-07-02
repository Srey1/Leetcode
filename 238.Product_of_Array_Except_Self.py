# Solution 1! - Using divides, beats 99% in terms of time and 50% in terms of memory
def productExceptSelf(self, nums: List[int]) -> List[int]:
    product = 1
    zero_count = 0
    # Count the number of zeros in nums as well as the total product of nums without any zeros
    for num in nums:
        if num == 0 and zero_count >= 1:
            zero_count = 2
            break
        elif num == 0 and zero_count == 0:
            zero_count += 1
        else:
            product *= num
    # If there are more than one zeros the product for everything must be zero
    if zero_count > 1:
        return [0] * len(nums)
    # If there is one zero then the product of all the non-zero numbers will be zero and the product of the zero will be the normal product without the zero
    elif zero_count == 1:
        return [product if num == 0 else 0 for num in nums]
    # If there are no zeros, then the product without each number is just the total product divided by that number
    else:
        return [product // num for num in nums]

# Solution 2! - Without using divides, beats 55% in terms of time and 99% in terms of memory
def productExceptSelf(self, nums: List[int]) -> List[int]:
    # Create output array
    output = [1] * len(nums)
    # Calculate prefixes and store them in the output array
    for i in range(1, len(nums)):
        output[i] = nums[i-1] * output[i-1]
    postfix = 1
    # Multiply the prefixes by the postfixes to get the final output
    for i in range(len(nums)-1, -1, -1):
        output[i] *= postfix
        postfix *= nums[i]
    return output


