/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let pre = strs[0];
    for (str of strs) {
        for (i in pre) {
            if (!str[i] || str[i] != pre[i]) {
                pre = str.substring(0, i);
                break;
            }
        }
    }
    return pre;
};