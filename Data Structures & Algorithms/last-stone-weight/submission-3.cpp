class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> heap(stones.begin(), stones.end());

        while (heap.size()>1){
            int x = heap.top();
            heap.pop();
            int y = heap.top();
            heap.pop();

            if (y<x){
                heap.push(x-y);
            }
        }

        if (heap.size()==0){
            return 0;
        }
        return heap.top();
    }
};
