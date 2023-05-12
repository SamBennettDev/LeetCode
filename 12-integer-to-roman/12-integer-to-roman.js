/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    let rom = "";
    while (num >= 1000) {
        num -= 1000;
        rom += "M";
    }
    while (num >= 500) {
        if (num >= 900) {
            rom += "CM";
            num -= 900;
            continue;
        }
        num -= 500;
        rom += "D";
    }
    while (num >= 100) {
        if (num >= 400) {
            rom += "CD";
            num -= 400;
            continue;
        }
        num -= 100;
        rom += "C";
    }
    while (num >= 50) {
        if (num >= 90) {
            rom += "XC";
            num -= 90;
            continue;
        }
        num -= 50;
        rom += "L";
    }
    while (num >= 10) {
        if (num >= 40) {
            rom += "XL";
            num -= 40;
            continue;
        }
        num -= 10;
        rom += "X";
    }
    while (num >= 5) {
        if (num >= 9) {
            rom += "IX";
            num -= 9;
            continue;
        }
        num -= 5;
        rom += "V";
    }
    while (num >= 1) {
        if (num >= 4) {
            rom += "IV";
            break;
        }
        num -= 1;
        rom += "I";
    }
    return rom;
};