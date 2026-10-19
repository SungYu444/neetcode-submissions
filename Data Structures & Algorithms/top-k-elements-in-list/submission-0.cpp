class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }

        vector<int> maxnums;
        for (int i = 0; i < k; i++) {
            auto max_it = max_element(count.begin(), count.end(), [](const auto& a, const auto& b) {
                return a.second < b.second;
            });
            maxnums.push_back(max_it->first);
            count.erase(max_it);
        }
        return maxnums;
    }
};
