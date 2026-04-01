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
        int n = 1000010;
        vector<int> del(n);
        for (auto &interval : intervals){
            ++del[interval.start];
            --del[interval.end];
        }
        // prefix sum - accumulate the count changes to find the count at each time
        for (int i = 0; i < n - 1; ++i){
            del[i+1] += del[i];
        }

        return *max_element(del.begin(), del.end());
    }
};
