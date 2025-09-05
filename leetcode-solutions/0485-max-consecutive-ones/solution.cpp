class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int maxCount = 0;
        int count = 0;

        for (int i : nums){
            if (i == 1){
                count = count + 1;
                maxCount = max(maxCount, count);
            }
            else{
                count = 0;
            }
        }

        return maxCount;
    }
};
