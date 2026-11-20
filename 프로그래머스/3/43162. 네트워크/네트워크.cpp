#include <string>
#include <vector>
#include <queue>

using namespace std;

void bfs(const vector<vector<int>>& computers,
         vector<bool>& visited,
         int start
        ){
    int n = computers.size();
    queue<int> q;
    q.push(start);
    
    while(!q.empty()){
        int cur = q.front(); q.pop();
        
        for(int i=0; i<n; i++){
            if(!visited[i] && computers[cur][i]) {
                visited[i] = true;
                q.push(i);
            }
        }
    }
    
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    
    vector<bool> visited(n, false);
    
    for(int i=0; i<n; i++){
        if(!visited[i]){
            visited[i] = true;
            bfs(computers, visited, i);
            answer++;
        }
    }
    
    return answer;
}