class Solution {
public:
    vector<int> gcdValues(vector<int>& nums, vector<long long>& queries) {
        int max_val = 0;
        for (int num : nums) {
            max_val = max(max_val, num);
        }

        vector<int> freq(max_val + 1, 0);
        for (int num : nums) {
            freq[num]++;
        }

        vector<long long> gcd_cnt(max_val + 1, 0);
        for (int i = max_val; i >= 1; --i) {
            long long c = 0;
            for (int j = i; j <= max_val; j += i) {
                c += freq[j];
            }
            gcd_cnt[i] = c * (c - 1) / 2;
            for (int j = 2 * i; j <= max_val; j += i) {
                gcd_cnt[i] -= gcd_cnt[j];
            }
        }

        vector<long long> pref(max_val + 1, 0);
        for (int i = 1; i <= max_val; ++i) {
            pref[i] = pref[i - 1] + gcd_cnt[i];
        }

        vector<int> ans;
        ans.reserve(queries.size());
        for (long long q : queries) {
            auto it = upper_bound(pref.begin(), pref.end(), q);
            ans.push_back(distance(pref.begin(), it));
        }

        return ans;
    }
};