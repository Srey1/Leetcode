public int romanToInt(String s) {
    HashMap<Character, Integer> convert = new HashMap<Character, Integer>();
    convert.put('I', 1);
    convert.put('V', 5);
    convert.put('X', 10);
    convert.put('L', 50);
    convert.put('C', 100);
    convert.put('D', 500);
    convert.put('M', 1000);
    int normalNum = 0;
    for (int i = 0; i < s.length(); i++) {
        if (i == s.length()-1 || convert.get(s.charAt(i)) >= convert.get(s.charAt(i+1))) {
            normalNum += convert.get(s.charAt(i));
        }
        else {
            normalNum -= convert.get(s.charAt(i));
        }
    }
    return normalNum;       
}