/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function(pattern, s) {
    const words = s.split(" ");
    if (words.length != pattern.length) return false;
    
    const used = new Set();
    const mapping = {};
    for(let i in pattern) {
        if (pattern[i] in mapping) {
            if (words[i] != mapping[pattern[i]]) return false;
        } else {
            if (used.has(words[i])) return false;
            mapping[pattern[i]] = words[i];
            used.add(words[i]);
        }
    }
    return true;
};