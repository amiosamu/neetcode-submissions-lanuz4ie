class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        vector<vector<int>> adj(n);

        for (int i = 0; i < edges.size(); i++){
            vector<int> edge = edges[i];
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        vector<bool> visited(n);

        int count = 0;
        for (int i = 0; i < n; i++){
            if (visited[i] == false){
                count++;
                dfs(adj, i, visited);
            }
        }
        return count;
    }
private:
    void dfs(vector<vector<int>>& adj, int index, vector<bool>& visited){
        visited[index] = true;
        for (auto i : adj[index]){
            if (visited[i] == false){
                dfs(adj, i, visited);
            }
        }
    }
};
