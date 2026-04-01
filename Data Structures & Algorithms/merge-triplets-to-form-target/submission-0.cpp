class Solution {
public:
    bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
        int d = 0;
        int e = 0;
        int f = 0;
        int targetX = target[0];
        int targetY = target[1];
        int targetZ = target[2];
        for (auto& triplet : triplets){
            int curX = triplet[0];
            int curY = triplet[1];
            int curZ = triplet[2];
            if (curX <= targetX  && curY <= targetY && curZ <= targetZ){
                d = max(d, curX);
                e = max(e, curY);
                f = max(f, curZ);
            }
        }
        return (d == targetX && e == targetY && f == targetZ);
    }
};
