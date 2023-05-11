/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    const mapping = {};
    const used = new Set();
    for (let i in t) {
        if (s[i] in mapping) {
            if (mapping[s[i]] != t[i]) return false;
        } else {
            if (used.has(t[i])) return false;
            mapping[s[i]] = t[i];
            used.add(t[i]);
        }
    }
    return true;
};