#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<vector<int>> board(102, vector<int>(102, 0));

int dr[4] = {-1,1,0,0};
int dc[4] = {0,0,-1,1};

struct Node {
    int r,c,len;
};

void drawLine(const vector<vector<int>>& rectangle){
    for(auto r : rectangle){
        int x1 = r[0] * 2;
        int y1 = r[1] * 2;
        int x2 = r[2] * 2;
        int y2 = r[3] * 2;
        
        for(int x = x1; x<= x2; x++){
            board[y1][x] = 1;
            board[y2][x] = 1;
        }
        
        for(int y = y1; y<=y2; y++){
            board[y][x1] = 1;
            board[y][x2] = 1;
        }
    }
    
    for (auto r : rectangle) {
        int x1 = r[0] * 2;
        int y1 = r[1] * 2;
        int x2 = r[2] * 2;
        int y2 = r[3] * 2;
        
        for(int i=y1+1; i<y2; i++){
            for(int j=x1+1; j<x2; j++){
                board[i][j] = 0;
            }
        }
    }
}

int bfs(int characterX, int characterY, int itemX, int itemY) {
    vector<vector<bool>> visited(102, vector<bool>(102, false));
    queue<Node> q;
    
    visited[characterY][characterX] = true;
    q.push({characterY, characterX, 0});
    
    while(!q.empty()){
        auto[r,c,len] = q.front(); q.pop();
        
        if(r==itemY && c==itemX) return len/2;
        
        for(int d=0; d<4; d++){
            int nr = r+dr[d];
            int nc = c+dc[d];
            
            if(0>nr||nr>=102||0>nc||nc>=102) continue;
            if(!board[nr][nc]) continue;
            if(visited[nr][nc]) continue;
            
            visited[nr][nc] = true;
            q.push({nr, nc, len+1});
            
        }
    }
    
    return 0;
    
}

int solution(vector<vector<int>> rectangle, int characterX, int characterY, int itemX, int itemY) {
    int answer = 0;
    
    drawLine(rectangle);
    
    return bfs(characterX*2, characterY*2, itemX*2, itemY*2);
}