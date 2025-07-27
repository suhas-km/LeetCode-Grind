use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut seen = HashMap::new();

        for (i, &value) in nums.iter().enumerate() {
            let remaining = target - value;
            if let Some(&j) = seen.get(&remaining) {
                return vec![i as i32, j as i32];
            }
            seen.insert(value, i);
        }

        vec![] // return an empty vector if no solution is found
    }
}

