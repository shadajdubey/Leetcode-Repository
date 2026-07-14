#include <vector>
#include <numeric>
#include <cstring>

class Solution {
private:
    int memo[201][201][201];
    const int MOD = 1e9 + 7;

    int solve(int i, int g1, int g2, const std::vector<int>& nums) {
        
        if (i == nums.size()) {
            
            return (g1 == g2 && g1 > 0) ? 1 : 0;
        }

        
        if (memo[i][g1][g2] != -1) {
            return memo[i][g1][g2];
        }

        
        long long ans = solve(i + 1, g1, g2, nums);

        
        int next_g1 = (g1 == 0) ? nums[i] : std::gcd(g1, nums[i]);
        ans = (ans + solve(i + 1, next_g1, g2, nums)) % MOD;

       
        int next_g2 = (g2 == 0) ? nums[i] : std::gcd(g2, nums[i]);
        ans = (ans + solve(i + 1, g1, next_g2, nums)) % MOD;

        return memo[i][g1][g2] = ans;
    }

public:
    int subsequencePairCount(std::vector<int>& nums) {
        
        std::memset(memo, -1, sizeof(memo));
        
       
        return solve(0, 0, 0, nums);
    }
};