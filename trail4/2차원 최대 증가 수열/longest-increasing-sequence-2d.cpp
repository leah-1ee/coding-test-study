#include <iostream>
#include <algorithm>

using namespace std;

int n, m;
int grid[51][51];
int dp[51][51];

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> grid[i][j];
        }
    }

    // Please write your code here.

    int ans = 0;
    dp[0][0] = 1;

    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            
            for(int r=0; r<i; r++){
                for(int c=0; c<j; c++){
                    if(dp[r][c] == 0) continue;
                    if(grid[i][j] <= grid[r][c]) continue;

                    dp[i][j] = max(dp[i][j], dp[r][c] + 1);
                }
            }

            ans = max(ans, dp[i][j]);
        }
    }

    cout << ans;

    return 0;
}
