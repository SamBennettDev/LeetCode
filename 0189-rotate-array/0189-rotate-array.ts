/**
 Do not return anything, modify nums in-place instead.
 */
function rotate(nums: number[], k: number): void {
    if (k == 0) return;
    

    let temps: number[] = nums.slice(0, k);

    for (let i: number = 0; i < nums.length; i++) {
        let newIndex: number = (i + k) % nums.length;
        let tempIndex = i % k;

        let temp: number = nums[newIndex];
        nums[newIndex] = temps[tempIndex];
        temps[tempIndex] = temp;
    }
};