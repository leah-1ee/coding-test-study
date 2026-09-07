#include <iostream>
#include <algorithm>

using namespace std;

int n;
int grid[100][100];

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
        }
    }

    // Please write your code here.

    int dp[n][n] = {};

    dp[0][n-1] = grid[0][n-1];

    for(int i=n-2; i>=0; i--){
        dp[0][i] = dp[0][i+1] + grid[0][i];
    }

    for(int i=1; i<n; i++){
        dp[i][n-1] = dp[i-1][n-1] + grid[i][n-1];
    }

    for(int i=1; i<n; i++){
        for(int j=n-2; j>=0; j--){
            dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j+1] + grid[i][j]);
        }
    }

    cout<<dp[n-1][0];

    return 0;
}
