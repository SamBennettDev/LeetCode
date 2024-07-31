function climbStairs(n: number): number {
    const memo = new Map<number, number>();

    function climb(n: number): number {
        if (n <= 3) return n;

        if (memo.has(n)) return memo.get(n);

        const result = climb(n - 1) + climb(n - 2);
        memo.set(n, result);
        return result;
    }

    return climb(n);
};