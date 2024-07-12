function majorityElement(nums: number[]): number {
    let candidate = 0;
    let count = 0;

    nums.forEach((num) => {
        if (num != candidate) {
            count--;
        } else {
            count++;
        }

        if (count <= 0) {
            candidate = num;
            count = 1;
        }
    })
    return candidate;
};