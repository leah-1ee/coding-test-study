#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>

using namespace std;

int n;
int grid[500][500];
int dp[500][500];

int dr[4] = {-1,1,0,0};
int dc[4] = {0,0,-1,1};

vector<tuple<int, int, int>> cells;

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
            cells.push_back({grid[i][j], i, j});
            dp[i][j] = 1;
        }
    }

    // Please write your code here.

    int best = 0;

    sort(cells.begin(), cells.end());

    for(auto cur:cells){
        int val = get<0>(cur);
        int r = get<1>(cur);
        int c = get<2>(cur);

        for(int d=0; d<4; d++){
            int nr = r+dr[d];
            int nc = c+dc[d];

            if(nr<0||nr>=n||nc<0||nc>=n) continue;

            if(grid[r][c] < grid[nr][nc]){
                dp[nr][nc] = max(dp[nr][nc], dp[r][c]+1);
                best = max(best, dp[nr][nc]);
            }
        }
    }

    cout<<best;

    return 0;
}
