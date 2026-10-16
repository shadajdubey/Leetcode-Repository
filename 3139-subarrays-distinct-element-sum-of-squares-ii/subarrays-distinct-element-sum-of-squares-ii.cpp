#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
    long long MOD = 1e9 + 7;
    
    struct Node {
        long long sum = 0;
        long long lazy = 0;
    };
    
    int n;
    vector<Node> tree;

    void push(int node, int l, int r) {
        if (tree[node].lazy != 0) {
            int mid = l + (r - l) / 2;
            long long lz = tree[node].lazy;
            
            tree[2 * node].lazy = (tree[2 * node].lazy + lz) % MOD;
            tree[2 * node].sum = (tree[2 * node].sum + lz * (mid - l + 1)) % MOD;
            
            tree[2 * node + 1].lazy = (tree[2 * node + 1].lazy + lz) % MOD;
            tree[2 * node + 1].sum = (tree[2 * node + 1].sum + lz * (r - mid)) % MOD;
            
            tree[node].lazy = 0;
        }
    }

    void update(int node, int l, int r, int ql, int qr, long long val) {
        if (ql > r || qr < l) return;
        if (ql <= l && r <= qr) {
            tree[node].sum = (tree[node].sum + val * (r - l + 1)) % MOD;
            tree[node].lazy = (tree[node].lazy + val) % MOD;
            return;
        }
        push(node, l, r);
        int mid = l + (r - l) / 2;
        update(2 * node, l, mid, ql, qr, val);
        update(2 * node + 1, mid + 1, r, ql, qr, val);
        tree[node].sum = (tree[2 * node].sum + tree[2 * node + 1].sum) % MOD;
    }

    long long query(int node, int l, int r, int ql, int qr) {
        if (ql > r || qr < l) return 0;
        if (ql <= l && r <= qr) return tree[node].sum;
        push(node, l, r);
        int mid = l + (r - l) / 2;
        return (query(2 * node, l, mid, ql, qr) + query(2 * node + 1, mid + 1, r, ql, qr)) % MOD;
    }

public:
    int sumCounts(vector<int>& nums) {
        n = nums.size();
        tree.assign(4 * n, Node());
        
        unordered_map<int, int> last;
        long long current_sum = 0;
        long long total_sum = 0;
        
        for (int j = 0; j < n; ++j) {
            int i = 0;
            if (last.find(nums[j]) != last.end()) {
                i = last[nums[j]] + 1;
            }
            
            long long prev_linear = query(1, 0, n - 1, i, j);
            long long add_val = (2 * prev_linear + (j - i + 1)) % MOD;
            current_sum = (current_sum + add_val) % MOD;
            
            update(1, 0, n - 1, i, j, 1);
            last[nums[j]] = j;
            
            total_sum = (total_sum + current_sum) % MOD;
        }
        
        return total_sum;
    }
};