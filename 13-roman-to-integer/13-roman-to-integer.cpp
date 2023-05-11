class Solution {
public:
    int romanToInt(string s) {
        int sum = 0;
        char prev = 'N';
        for (char& numeral : s) {
            switch (numeral) {
                case 'I':
                    sum += 1;
                    break;
                case 'V':
                    if (prev == 'I') sum -= 2;
                    sum += 5;
                    break;
                case 'X':
                    if (prev == 'I') sum -= 2;
                    sum += 10;
                    break;
                case 'L':
                    if (prev == 'X') sum -= 20;
                    sum += 50;
                    break;
                case 'C':
                    if (prev == 'X') sum -= 20;
                    sum += 100;
                    break;
                case 'D':
                    if (prev == 'C') sum -= 200;
                    sum += 500;
                    break;
                case 'M':
                    if (prev == 'C') sum -= 200;
                    sum += 1000;
                    break;
            }
            prev = numeral;
        }
        return sum;
    }
};