class Solution {
public:
    int numDistinct(string s, string t) {
        int tLen = t.size();
        unsigned long long dp[tLen+1];
        memset(dp, 0, sizeof(dp));
        dp[0] = 1;
        for (char& sChar: s) {
            for (int i = tLen; i > 0; i--){
                char tChar = t[i-1];
                if (sChar == tChar){
                    dp[i] += dp[i-1];
                }
            }
        }
        return dp[tLen];
    }
};
