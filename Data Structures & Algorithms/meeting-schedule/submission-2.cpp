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
    bool canAttendMeetings(vector<Interval>& intervals) {
        sort(intervals.begin(), intervals.end(), 
            [](const Interval& a, Interval& b) {
                return a.start < b.start;
            });
        int cur_end = 0;
        for (auto inter : intervals){
            if (inter.start < cur_end){
                return false;
            }
            cur_end = inter.end;
        }
        return true;
    }
};
