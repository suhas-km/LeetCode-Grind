import java.util.HashMap;

class Solution {
    public boolean containsDuplicate(int[] nums) {

        HashMap<Integer, Integer> seen  = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            if(seen.containsKey(nums[i])){
                return true;
            }
            else{
                seen.put(nums[i], i);
            }
        }
        return false;
    }
}
