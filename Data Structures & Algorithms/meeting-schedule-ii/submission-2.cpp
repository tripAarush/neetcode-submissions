/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        sort(intervals.begin(), intervals.end(),
            [] (const Interval& a, Interval& b) {
                return a.start < b.start;
            });
        priority_queue<int, vector<int>, greater<int>> heap;
        int res = 0;
        for (auto inter : intervals){
            if (!heap.empty() and heap.top() <= inter.start){
                heap.pop();
                heap.push(inter.end);
            }
            else{
                heap.push(inter.end);
            }
            res = max(res, int(heap.size()));
        }
        return res;
    }
};
