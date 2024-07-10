/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let last = nums.length - 1;
    let i = 0;

    while (i <= last) {
        if (nums[i] == val) {
            nums[i] = nums[last];
            last--;
            i--;
        }
        i++;
    }

    return last + 1;
};