#include <iostream>
#include <algorithm>

using namespace std;

int n;
int profit[101];
int dp[101];

int main() {
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> profit[i];
    }

    // Please write your code here.
    for(int i=1; i<=n; i++){
        for (int j=1; j<=i; j++){
            dp[i] = max(dp[i], dp[i-j] + profit[j]);
        }
    }

    cout << dp[n];


    return 0;
}
