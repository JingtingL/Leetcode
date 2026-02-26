class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> charSet;
        int l = 0;
        int res = 0;

        for(int r=0; r < (int)s.size(); r++){
            while (charSet.count(s[r])){
                charSet.erase(s[l]);
                l += 1;
            }
            charSet.insert(s[r]);
            res = max(res, (int)charSet.size());
        }
        return res;
    }
};