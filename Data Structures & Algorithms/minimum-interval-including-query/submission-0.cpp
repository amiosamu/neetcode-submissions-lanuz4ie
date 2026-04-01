class Solution {
public:
    std::vector<int> minInterval(std::vector<std::vector<int>>& intervals, std::vector<int>& queries) {
        std::sort(intervals.begin(), intervals.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[0] < b[0];
        });

        std::vector<int> sortedQueries = queries;
        std::sort(sortedQueries.begin(), sortedQueries.end());
        std::map<int, int> res;

        auto cmp = [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[0] > b[0] || (a[0] == b[0] && a[1] > b[1]);
        };
        std::priority_queue<std::vector<int>, std::vector<std::vector<int>>, decltype(cmp)> minHeap(cmp);

        int i = 0;
        for (int q : sortedQueries) {
            while (i < intervals.size() && intervals[i][0] <= q) {
                int l = intervals[i][0];
                int r = intervals[i][1];
                minHeap.push({r - l + 1, r});
                i++;
            }

            while (!minHeap.empty() && minHeap.top()[1] < q) {
                minHeap.pop();
            }

            res[q] = minHeap.empty() ? -1 : minHeap.top()[0];
        }
        
        std::vector<int> result(queries.size());
        for (int j = 0; j < queries.size(); j++) {
            result[j] = res[queries[j]];
        }
        return result;
    }
};
