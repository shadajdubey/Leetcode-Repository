class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        vector<int> sorted_arr = arr;
        sort(sorted_arr.begin(), sorted_arr.end());
        
        unordered_map<int, int> ranks;
        int rank = 1;
        for (int num : sorted_arr) {
            if (ranks.find(num) == ranks.end()) {
                ranks[num] = rank++;
            }
        }
        
        for (int& num : arr) {
            num = ranks[num];
        }
        
        return arr;
    }
};