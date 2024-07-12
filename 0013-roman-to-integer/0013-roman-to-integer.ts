function romanToInt(s: string): number {
    let count: number = 0;

    for (let i: number = 0; i < s.length; i++) {
        switch (s[i]) {
            case "I":
                if (s[i + 1] == "V" || s[i + 1] == "X") {
                    count--;
                    break;
                }
                count++;
                break;
            case "V":
                count += 5;
                break;
            case "X":
                if (s[i + 1] == "L" || s[i + 1] == "C") {
                    count -= 10;
                    break;
                }
                count += 10;
                break;
            case "L":
                count += 50;
                break;
            case "C":
                if (s[i + 1] == "D" || s[i + 1] == "M") {
                    count -= 100;
                    break;
                }
                count += 100;
                break;
            case "D":
                count += 500;
                break;
            case "M":
                count += 1000;
                break;
        }
    }

    return count;
};