#include <iostream>

using namespace std;

int n;

int main() {
    cin >> n;

    // Please write your code here.
    // N = 1*a + 2*b
    // N=1 -> 1 
    // N=2 -> (1x2 or 2x1) -> 2 
    // N=3 -> 111 21 12 -> 3
    // N=4 -> 1111 211 121 112 22 -> 5
    // N=5 -> 11111 2111 1211 1121 1112 221 212 122 -> 8

    int dp[n+1];
    for(int i=0; i<=n; i++){
        dp[i] = 0;
    }

    dp[1] = 1;
    dp[2] = 2;

    for(int i=3; i<=n; i++){
        dp[i] = (dp[i-1] + dp[i-2]) % 10007;
    }

    cout << dp[n];

    return 0;
}
