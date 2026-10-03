/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverse_ll(ListNode* head) {
        ListNode *cur = head;
        ListNode *prev = nullptr;

        while (cur) {
            ListNode *nxt = cur->next;
            cur->next = prev;
            prev = cur;
            cur = nxt;
        }
        return prev;
    }
    void reorderList(ListNode* head) {
        // reverse 2nd half of ll
        // if odd lengths, include middle in 2nd half
        // if even, keep middle in first half
        // in odd, fast = None, even fast.next = None
        // odd cases include slow points, even start slow.next
        if (!head) {
            return;
        }
        ListNode *slow = head, *fast = head->next;
        while (fast and fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode *second = nullptr;
        second = reverse_ll(slow->next);
        slow->next = nullptr;

        bool f = false;
        ListNode *first = head->next, *res = head;
        while (first and second){
            if (!f) {
                res->next = second;
                second = second->next;
            }
            else {
                res->next = first;
                first = first->next;
            }
            f = !f;
            res = res->next;
        }
        if (first){
            res->next = first;
        }
        if (second){
            res->next = second;
        }
        return;
    }
};
