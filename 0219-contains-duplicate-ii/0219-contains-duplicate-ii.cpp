class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> seen = {}; // key is the number, value is the index

        for(int i=0; i < nums.size(); i++){
            auto lookup = seen.find(nums[i]);
            int space = 0;
            if (lookup != seen.end() && i - lookup->second <= k){
                return true;
            }
            seen[nums[i]] = i;
        }

        return false;
    }
};