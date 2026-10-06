#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int n, m, r, c;

int dr[4] = {-1,1,0,0};
int dc[4] = {0,0,-1,1};

vector<pair<int, int>> bombs;

int grid[101][101] = {};

int main() {
    cin >> n >> m >> r >> c;

    // Please write your code here.
    bombs.push_back({r-1, c-1});
    grid[r-1][c-1] = 1;

    for(int t=1; t<=m; t++){
        vector<pair<int, int>> currentBombs = bombs;
        int len = pow(2, t-1);

        for(auto[cr, cc]:currentBombs){
            for(int d=0; d<4; d++){
                int nr = cr + dr[d] * len;
                int nc = cc + dc[d] * len;

                if(nr<0 || nr>=n || nc<0 || nc>=n) continue;
                if(grid[nr][nc] == 1) continue;

                bombs.push_back({nr, nc});
                grid[nr][nc] = 1;
            }
        }
    }

    int cnt = 0;
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(grid[i][j] == 1) cnt++;
        }
    }

    cout<<cnt;

    return 0;
}
