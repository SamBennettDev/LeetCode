class Solution {
public:
    bool isSubsequence(string s, string t) {
        int sIndex = 0;
        int tIndex = 0;

        while (sIndex < s.length()) {
            if (tIndex >= t.length()) {
                return false;
            }

            if (s[sIndex] != t[tIndex]) {
                tIndex++;
                continue;
            }

            sIndex++;
            tIndex++;
        }

        return true;
    }
};