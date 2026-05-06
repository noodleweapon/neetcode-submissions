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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode* prev = nullptr;
        ListNode* curr = head;

        vector<ListNode*> points(4, nullptr);

        int pos = 0;
        while (curr != nullptr) {
            ++pos;
            if (pos == left - 1) points[0] = curr;
            if (pos == left) points[1] = curr;
            if (pos == right) points[2] = curr;
            if (pos == right + 1) points[3] = curr;

            ListNode* nxt = curr->next;

            if ((pos > left) && (pos <= right)) {
                curr->next = prev;
            }

            prev = curr;
            curr = nxt;
        }
        if ((points[0] != nullptr) && (points[2] != nullptr)) {
            points[0]->next = points[2];
        }
        if ((points[1] != nullptr) && (points[3] != nullptr)) {
            points[1]->next = points[3];
        }
        if (points[0] == nullptr) {
            return points[2];
        } else {
            return head;
        }
    }
};