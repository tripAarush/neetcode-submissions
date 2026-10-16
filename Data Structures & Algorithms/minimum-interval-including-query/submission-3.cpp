#include <iostream>
class Solution {
public:
    vector<int> minInterval(vector<vector<int>>& intervals, vector<int>& queries) {
        sort(intervals.begin(), intervals.end());
        vector<int> sort_q(queries); 
        sort(sort_q.begin(), sort_q.end());
        priority_queue<tuple<int,int,int>, vector<tuple<int,int,int>>, greater<tuple<int,int,int>>> heap;
        int i = 0;
        unordered_map<int, int> hashmap;
        for (const auto& q : sort_q){
            while (i<intervals.size() and intervals[i][0] <= q){
                heap.push({intervals[i][1]-intervals[i][0]+1, intervals[i][0], intervals[i][1]});
                i++;
            }
            while (!heap.empty() and get<2>(heap.top())<q){
                heap.pop();
            }
            if (!heap.empty()){
                hashmap[q] = get<0>(heap.top());
            } else {
                hashmap[q] = -1;
            }
        }
        vector<int> res = {};
        for (int i=0; i<queries.size();i++){
            res.push_back(hashmap[queries[i]]);
        }
        return res;
    }
};
