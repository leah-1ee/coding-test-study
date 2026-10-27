#include <iostream>
#include <algorithm>

using namespace std;

int n, m;
int A[100];
int dp[10001];

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    // Please write your code here.
    dp[0] = 0;

    for (int i=1; i<=m; i++){
        dp[i] = -1;
    }

    for (int i=0; i<n; i++){
        for(int j=m; j>=0; j--){
            if (j< A[i]) continue;
            if (dp[j-A[i]] == -1) continue;

            if(dp[j] == -1) dp[j] = dp[j-A[i]] + 1;
            else dp[j] = min(dp[j], dp[j-A[i]] + 1);
        }
    }

    cout << dp[m];

    return 0;
}
