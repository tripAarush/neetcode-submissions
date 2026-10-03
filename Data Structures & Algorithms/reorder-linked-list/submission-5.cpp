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
    void reorderList(ListNode* head) {
        if (!head){
            return;
        }
        ListNode *slow = head, *fast = head;
        while (fast and fast->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode *second = slow->next;
        slow->next = nullptr;
        
        ListNode *prev = nullptr;
        while(second){
            ListNode *nxt = second->next;
            second->next = prev;
            prev = second;
            second = nxt;
        }
        second = prev;

        ListNode *first = head;
        
        while (second){
            ListNode *next1 = first->next;
            ListNode *next2 = second->next;

            first->next = second;
            second->next = next1;

            first = next1;
            second = next2;
        }

    }
};
