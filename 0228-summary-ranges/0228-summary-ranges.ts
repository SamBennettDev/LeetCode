function summaryRanges(nums: number[]): string[] {
    const range: string[] = [];
    let current: number = nums[0];

    if (nums.length == 1) {
        range.push(nums[0].toString());
    }

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] != nums[i - 1] + 1) {
            if (current == nums[i - 1]) {
                range.push(current.toString());
            }
            else {
                range.push(current.toString() + "->" + nums[i - 1].toString());
            }

            current = nums[i];
        }

        if (i == nums.length - 1) {
            if (current == nums[i]) {
                range.push(current.toString());
            }
            else {
                range.push(current.toString() + "->" + nums[i].toString());
            }
        }
    }

    return range;
};