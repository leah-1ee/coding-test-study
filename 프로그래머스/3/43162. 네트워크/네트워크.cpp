#include <string>
#include <vector>
#include <queue>

using namespace std;

void bfs(const vector<vector<int>>& computers,
        int start,
        vector<bool>& visited,
        int n){
    visited[start] = true;
    
    queue<int> q;
    q.push(start);
    
    while(!q.empty()){
        int cur = q.front(); q.pop();
        for(int next = 0; next<n; next++){
            if(computers[cur][next] == 0) continue;
            if(visited[next]) continue;
            visited[next] = true;
            q.push(next);
        }
    }
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    
    vector<bool> visited(n);
    
    for(int i=0; i<n; i++){
        if(!visited[i]) {
            bfs(computers, i, visited, n);
            answer++;
        }
    }
    
    return answer;
}