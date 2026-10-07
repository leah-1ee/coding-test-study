#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, m, t, k;

struct Marble {
    int r, c, dir, speed;
    bool alive;
};

Marble marbles[2501];
vector<int> grid[51][51];

// 0<->2 , 1<->3
// 상 좌 하 우
int dr[4] = {-1, 0, 1, 0};
int dc[4] = {0, -1, 0, 1};

int getDir(char d){
    if(d=='U') return 0;
    if(d=='L') return 1;
    if(d=='D') return 2;
    return 3;
}

void moveMarbles() {
    vector<int> nextGrid[51][51];

    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(grid[i][j].size() == 0) continue;

            for(int cur : grid[i][j]){
                auto &[r,c,dir,speed,alive] = marbles[cur];

                if(!alive) continue;
                for(int s=0; s<speed; s++){
                    int nr = r+dr[dir];
                    int nc = c+dc[dir];

                    if(nr<0 || nr>=n || nc<0 || nc>=n) {
                        dir = (dir+2) % 4;
                        nr = r+dr[dir];
                        nc = c+dc[dir];
                    }

                    r = nr; c = nc;
                }

                nextGrid[r][c].push_back(cur);
            }
        }
    }
    
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            grid[i][j] = nextGrid[i][j];
        }
    }
}

bool cmp (int a, int b){
    if(marbles[a].speed != marbles[b].speed)
        return marbles[a].speed > marbles[b].speed;
    
    return a>b;
}

void removeMarbles() {
    for(int i=0; i<n ;i ++){
        for(int j=0; j<n ;j++){
            if(grid[i][j].size() <= k) continue;

            sort(grid[i][j].begin(), grid[i][j].end(), cmp);

            while(grid[i][j].size() > k) {
                int idx = grid[i][j].back();
                marbles[idx].alive = false;
                grid[i][j].pop_back();
            }
        }
    }
}

int main() {
    cin >> n >> m >> t >> k;

    for (int i = 1; i <= m; i++) {
        int r, c, v;
        char d;
        cin>>r>>c>>d>>v;
        r--; c--;

        int dir = getDir(d);

        marbles[i] = {r, c, dir, v, true};
        grid[r][c].push_back(i);
    }

    // Please write your code here.
    for(int i=0; i<t; i++){
        moveMarbles();
        removeMarbles();
    }

    int cnt = 0;
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cnt += grid[i][j].size();
        }
    }

    cout<<cnt;

    return 0;
}
