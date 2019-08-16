/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution
{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        ListNode *res = new ListNode(0);
        ListNode *temp = res;
        int tot = 0;
        int carry = 0;
        while (l1 && l2)
        {
            tot = carry + (l1->val) + (l2->val);
            if (tot < 10)
            {
                res->next = new ListNode(tot);
                carry = 0;
            }
            else
            {
                res->next = new ListNode(tot % 10);
                carry = tot / 10;
            }
            l1 = l1->next;
            l2 = l2->next;
            res = res->next;
        }
        while (l1)
        {
            tot = carry + l1->val;
            if (tot < 10)
            {
                res->next = new ListNode(tot);
                carry = 0;
            }
            else
            {
                res->next = new ListNode(tot % 10);
                carry = tot / 10;
            }
            l1 = l1->next;
            res = res->next;
        }
        while (l2)
        {
            tot = carry + l2->val;
            if (tot < 10)
            {
                res->next = new ListNode(tot);
                carry = 0;
            }
            else
            {
                res->next = new ListNode(tot % 10);
                carry = tot / 10;
            }
            l2 = l2->next;
            res = res->next;
        }
        if (carry > 0)
        {
            res->next = new ListNode(carry);
        }
        return temp->next;
    }
};