/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    unordered_map<Node*, Node*> self_to_new;
    Node* dfs(Node* node){
        if (!node) {
            return nullptr;
        }
        if (self_to_new.count(node)){
            return self_to_new[node];
        }

        Node* copy = new Node(node->val);
        self_to_new[node] = copy;

        copy->next = dfs(node->next);
        copy->random = dfs(node->random);

        return copy;
    }
    Node* copyRandomList(Node* head) {
        return dfs(head);
    }
};
