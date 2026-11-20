#include <vector>
#include <queue>
using namespace std;

int dr[4] = {-1,1,0,0};
int dc[4] = {0,0,-1,1};

struct Node{
    int r, c, len;
};

int bfs(const vector<vector<int>>& maps){
    int n = maps.size();
    int m = maps[0].size();
    
    vector<vector<bool>> visited(n, vector<bool>(m, false));
    queue<Node> q;
    
    visited[0][0] = true;
    q.push({0, 0, 1});
    
    while(!q.empty()){
        auto[r, c, len] = q.front(); q.pop();
        if(r==n-1 && c==m-1) return len;
        
        for(int d=0; d<4; d++){
            int nr = r+dr[d];
            int nc = c+dc[d];
            
            if(nr<0 || nr>=n || nc<0 || nc>=m) continue;
            if(maps[nr][nc]==0) continue;
            if(visited[nr][nc]) continue;
            visited[nr][nc] = true;
            q.push({nr, nc, len+1});
            
        }
        
    }
    return -1;
    
}

int solution(vector<vector<int>> maps)
{
    
    return bfs(maps);
}