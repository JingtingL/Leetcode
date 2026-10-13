class Solution {
public:
    bool isAnagram(string s, string t) {
        // establish a little chart for counting 26 characters
        // using array which is on the stack
        int count[26] = {};

        for (char c: s){
            count[c - 'a']++;
        }

        for (char c: t){
            count[c - 'a']--;
        }

        for (int i: count){
            if (i != 0){
                return false;
            }
        }

        return true;
    }
};