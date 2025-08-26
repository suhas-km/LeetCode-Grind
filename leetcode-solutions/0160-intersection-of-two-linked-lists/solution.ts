/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function getIntersectionNode(headA: ListNode | null, headB: ListNode | null): ListNode | null {
    let l1: ListNode | null = headA;
    let l2: ListNode | null = headB;

    while (l1 !== l2) {
        l1 = l1 ? l1.next : headB;
        l2 = l2 ? l2.next : headA;
    }

    return l2;
}
