#include <string>
#include <vector>
#include <queue>

using namespace std;

int bfs(const vector<vector<int>>& graph) {
    queue<int> q;
    vector<bool> visited(graph.size(), false);
    
    q.push(1);
    visited[1] = true;
    
    int count = 0;
    
    while(!q.empty()){
        int cur = q.front(); q.pop();
        count++;
        
        for(int next:graph[cur]){
            if(visited[next]) continue;
            visited[next] = true;
            q.push(next);
        }
    }
    return count;
}

int solution(int n, vector<vector<int>> wires) {
    int minDiff = n;
    
    for(int i=0; i<wires.size(); i++){
        vector<vector<int>> graph(n+1);
        
        for(int j=0; j<wires.size(); j++){
            if(i==j) continue;
            
            int a = wires[j][0];
            int b = wires[j][1];
            
            graph[a].push_back(b);
            graph[b].push_back(a);
        }
        
        // bfs
        int count = bfs(graph);
        int diff = abs(count - (n - count));
        
        minDiff = min(minDiff, diff);
        
    }
    
    
    
    return minDiff;
}