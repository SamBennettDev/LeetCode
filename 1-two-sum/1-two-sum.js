/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const numAndIndex = {};
    const y = 0;
    for (let i in nums) {
        numAndIndex[nums[i]] = i;
    }
    for (let i in nums) {
        const y = target - nums[i];
        if (y in numAndIndex && i != numAndIndex[y]) {
            return [i, numAndIndex[y]];
        }
    }
};