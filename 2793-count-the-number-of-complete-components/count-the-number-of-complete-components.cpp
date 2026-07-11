#include <vector>

class Solution {
public:
    void dfs(int node, const std::vector<std::vector<int>>& adj, std::vector<bool>& visited, int& vertexCount, int& edgeCount) {
        visited[node] = true;
        vertexCount++;
        edgeCount += adj[node].size();
        
        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                dfs(neighbor, adj, visited, vertexCount, edgeCount);
            }
        }
    }

    int countCompleteComponents(int n, std::vector<std::vector<int>>& edges) {
        std::vector<std::vector<int>> adj(n);
        for (const auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }

        std::vector<bool> visited(n, false);
        int completeComponents = 0;

        for (int i = 0; i < n; ++i) {
            if (!visited[i]) {
                int vertexCount = 0;
                int edgeCount = 0;
                dfs(i, adj, visited, vertexCount, edgeCount);
                
                if (edgeCount == vertexCount * (vertexCount - 1)) {
                    completeComponents++;
                }
            }
        }

        return completeComponents;
    }
};