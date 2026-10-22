class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> seen;
        seen[0] = 1;
        
        int running_total = 0;
        int count = 0;

        for(int i=0; i<nums.size(); i++){
            running_total += nums[i];
            int target = running_total - k;

            if(seen.count(target)){
                count += seen.find(target)->second;
            }

            seen[running_total]++;
        }

        return count;
    }
};