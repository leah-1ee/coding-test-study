#include <iostream>
#include <algorithm>

using namespace std;

int n;
int grid[101][101];

int minVal = 101;
int maxVal = 0;

bool possible(int mid) {
    for(int low = minVal; low<=maxVal - mid; low++){
        bool dp[101][101];
        int high = low + mid;

        if(grid[0][0] < low || grid[0][0] > high) continue;

        dp[0][0] = true;

        for(int i=1; i<n; i++){
            if(grid[i][0] < low || grid[i][0] > high) dp[i][0] = false;
            else if (dp[i-1][0] == false) dp[i][0] = false;
            else dp[i][0] = true;

            if(grid[0][i] < low || grid[0][i] > high) dp[0][i] = false;
            else if (dp[0][i-1] == false) dp[0][i] = false;
            else dp[0][i] = true;
        }

        for(int i=1; i<n; i++){
            for(int j=1; j<n; j++){
                if(grid[i][j] < low || grid[i][j] > high) dp[i][j] = false;
                else if (dp[i][j-1] == false && dp[i-1][j] == false) dp[i][j] = false;
                else dp[i][j] = true;
            }
        }

        if(dp[n-1][n-1]) return true;
    }

    return false;

}

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
            minVal = min(minVal, grid[i][j]);
            maxVal = max(maxVal, grid[i][j]);
        }
    }

    // Please write your code here.

    int left = 0;
    int right = maxVal - minVal;

    while(left < right) {
        int mid = (left + right) / 2;

        if(possible(mid)) right = mid;
        else left = mid+1;
    }

    cout<<left;

    return 0;
}

