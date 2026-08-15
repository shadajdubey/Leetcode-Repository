class Solution {
public:
    int longestSubsequence(vector<int>& nums) {
        int total_xor = 0;
        bool has_non_zero = false;

        for (int x : nums) {
            total_xor ^= x;
            if (x > 0) {
                has_non_zero = true;
            }
        }

        if (total_xor != 0) {
            return nums.size();
        }
        if (!has_non_zero) {
            return 0;
        }
        return nums.size() - 1;
    }
};