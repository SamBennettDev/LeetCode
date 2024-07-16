class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        if (magazine.size() < ransomNote.size())
            return false;

        for (int i = 0; i < ransomNote.size(); i++) {
            for (int j = 0; j < magazine.size(); j++) {
                if (ransomNote[i] == magazine[j]) {
                    magazine.erase(j, 1);
                    break;
                }
                if (j == magazine.size() - 1)
                    return false;
            }
        }
        return true;
    }
};