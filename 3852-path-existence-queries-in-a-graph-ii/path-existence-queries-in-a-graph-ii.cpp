#include <vector>
#include <numeric>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
public:
    vector<int> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {
        vector<int> p(n);
        iota(p.begin(), p.end(), 0);
        sort(p.begin(), p.end(), [&](int i, int j) {
            return nums[i] < nums[j];
        });

        vector<int> pos(n);
        for (int i = 0; i < n; ++i) {
            pos[p[i]] = i;
        }

        vector<int> comp(n, 0);
        int c = 0;
        for (int i = 1; i < n; ++i) {
            if (nums[p[i]] - nums[p[i - 1]] > maxDiff) {
                c++;
            }
            comp[i] = c;
        }

        vector<int> next_hop(n);
        int r = 0;
        for (int i = 0; i < n; ++i) {
            while (r < n && nums[p[r]] - nums[p[i]] <= maxDiff && comp[r] == comp[i]) {
                r++;
            }
            next_hop[i] = r - 1;
        }

        int max_k = 20;
        vector<vector<int>> up(max_k, vector<int>(n));
        for (int i = 0; i < n; ++i) {
            up[0][i] = next_hop[i];
        }

        for (int k = 1; k < max_k; ++k) {
            for (int i = 0; i < n; ++i) {
                up[k][i] = up[k - 1][up[k - 1][i]];
            }
        }

        vector<int> ans;
        ans.reserve(queries.size());

        for (const auto& q : queries) {
            int u = pos[q[0]];
            int v = pos[q[1]];

            if (u == v) {
                ans.push_back(0);
                continue;
            }

            if (comp[u] != comp[v]) {
                ans.push_back(-1);
                continue;
            }

            if (u > v) {
                swap(u, v);
            }

            int steps = 0;
            for (int k = max_k - 1; k >= 0; --k) {
                if (up[k][u] < v) {
                    steps += (1 << k);
                    u = up[k][u];
                }
            }
            ans.push_back(steps + 1);
        }

        return ans;
    }
};