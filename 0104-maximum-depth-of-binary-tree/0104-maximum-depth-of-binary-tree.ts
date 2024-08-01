/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function maxDepth(root: TreeNode | null): number {
    if (!root) return 0;

    const queue: Array<[TreeNode, number]> = [[root, 1]]; 
    let max = 1;
    
    while (queue.length > 0) {
        if (max < queue[0][1]) {
            max = queue[0][1];
        }

        if (queue[0][0].left) {
            queue.push([queue[0][0].left, queue[0][1] + 1])
        }

        if (queue[0][0].right) {
            queue.push([queue[0][0].right, queue[0][1] + 1])
        }

        queue.shift();
    }

    return max;
};