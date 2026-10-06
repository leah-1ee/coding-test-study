#include <iostream>
#include <deque>

using namespace std;

int N, M, K;
int x[10000], y[10000];
char d[1000];
int p[1000];

int grid[101][101] = {};
deque<pair<int, int>> dq;

int dr[4] = {-1,1,0,0};
int dc[4] = {0,0,-1,1};

bool move(int dir) {
    auto head = dq.front(); 
    int r = head.first;
    int c = head.second;

    int nr = r + dr[dir];
    int nc = c + dc[dir];

    if(nr<0 || nr>=N || nc<0 || nc>= N) return false;

    if(grid[nr][nc] != 2) {
        auto back = dq.back();
        int br = back.first;
        int bc = back.second;
        grid[br][bc] = 0;
        dq.pop_back();
    } 

    if(grid[nr][nc] == 1) return false;

    dq.push_front({nr, nc});
    grid[nr][nc] = 1;

    return true;
}

int main() {
    cin >> N >> M >> K;

    for (int i = 0; i < M; i++) cin >> x[i] >> y[i];

    for (int i = 0; i < K; i++) cin >> d[i] >> p[i];

    // Please write your code here.
    int time = 1;
    for(int i=0; i<M; i++){
        grid[x[i]-1][y[i]-1] = 2;
    }

    dq.push_front({0,0});

    int dir;
    for(int i=0; i<K; i++){
        if(d[i]=='U') dir = 0;
        if(d[i]=='D') dir = 1;
        if(d[i]=='L') dir = 2;
        if(d[i]=='R') dir = 3;

        for(int j=0; j<p[i]; j++){
            if(move(dir)) {
                time++;
                continue;
            }
            cout << time;
            return 0;
        }
    }

    cout<<time-1;

    return 0;
}
