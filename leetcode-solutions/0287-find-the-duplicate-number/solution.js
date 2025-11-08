/**
 * @param {number[]} nums
 * @return {number}
 */

var findDuplicate = function(nums) {
  const seen = new Set();
  
  for (let i = 0; i < nums.length; i++){
    const num = nums[i];

    if (seen.has(num)){
      return num;
    }
    else{
      seen.add(num);
    }
  }
};

