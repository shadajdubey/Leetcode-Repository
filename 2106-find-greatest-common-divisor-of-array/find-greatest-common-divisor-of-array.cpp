#include <vector>
#include <algorithm>
#include <numeric>

class Solution {
public:
    int findGCD(std::vector<int>& nums) {
        auto [mn, mx] = std::minmax_element(nums.begin(), nums.end());
        return std::gcd(*mn, *mx);
    }
};