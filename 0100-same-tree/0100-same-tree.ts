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

function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
    if (!p && !q) return true;
    else if (!p || !q) return false;

    const queue: Array<[TreeNode, TreeNode]> = [[p, q]];

    while (queue.length > 0) {
        if (queue[0][0].val != queue[0][1].val) {
            return false;
        }

        if (queue[0][0].left && queue[0][1].left) {
            queue.push([queue[0][0].left, queue[0][1].left]);
        } 
        else if (queue[0][0].left || queue[0][1].left) {
            return false;
        }

        if (queue[0][0].right && queue[0][1].right) {
            queue.push([queue[0][0].right, queue[0][1].right]);
        } 
        else if (queue[0][0].right || queue[0][1].right) {
            return false;
        }

        queue.shift();
    }

    return true;
};