class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        // I want to keep track of whether I have seen this specific letter before
        int seen[26] = {};

        for(char c: magazine){
            seen[c-'a']++;
        }

        for(char c: ransomNote){
            seen[c-'a']--;
        }

        for(int freq: seen){
            if (freq < 0){
                return false;
            }
        }

        return true;
    }
};