public boolean isPalindrome(int x) {
    // Any negative number cannot be a palindrome
    if (x < 0) {
        return false;
    }
    // This will store the reverse of the number
    int reverse = 0;
    // Store the value of x so we can compare the reverse to it later
    int storeX = x;
    // While x is not 0 do the following
    while (x != 0) {
        // Multiply the current reverse by 10 (so increase the magnitude) and then add on the last digit of x. By doing this we create the reverse as the last digit of x will become the first digit of the reverse as it is multiplied by 10 so much
        reverse = (reverse * 10) + (x % 10);
        // Ensure to chalk off the last digit of x
        x /= 10;
    }
    // Return if the reversed number equals the original number x
    return (reverse == storeX);
    
    
}
