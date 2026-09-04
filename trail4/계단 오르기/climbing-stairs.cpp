#include <iostream>

using namespace std;

int n;

int main() {
    cin >> n;

    // Please write your code here.
    // dp[i]: i층에 도달하는 경우의 수

    int dp[n+1];

    for(int i=0; i<=n; i++){
        dp[i] = 0;
    }

    if(n==2 || n==3) {
        cout<<1;
        return 0;
    }

    dp[2] = 1;
    dp[3] = 1;

    for(int i=4; i<=n; i++){
        dp[i]  = (dp[i-2] + dp[i-3]) % 10007;
        //cout<<i<<" "<<dp[i]<<'\n';
    }

    cout<<((dp[n]==0) ? 0 : dp[n] % 10007);

    return 0;
}