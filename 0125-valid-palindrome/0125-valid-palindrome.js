/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    arr = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase().split('');
    
    let j = arr.length - 1;

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] != arr[j]) {
            return false;
        }
        j--;
    }

    return true;
};