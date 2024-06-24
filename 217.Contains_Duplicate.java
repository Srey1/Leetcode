public boolean containsDuplicate(int[] nums) {
    Set<Integer> hash_Set = new HashSet<Integer>(); 
    for (int i : nums) {
            if (!hash_Set.add(i))
            return true;
    }
    return false;        
}