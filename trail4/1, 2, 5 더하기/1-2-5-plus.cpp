#include <iostream>
#include <algorithm>

using namespace std;

int n;
int list[3] = {1,2,5};
int dp[1001];

int main() {
    cin >> n;

    // Please write your code here.
    dp[0] = 1;

    for(int i=1; i<=n; i++){
        dp[i] = 0;

        for(int j=0; j<3; j++){
            if(i<list[j]) continue;
            if(dp[i-list[j]] == -1) continue;

            dp[i] = (dp[i] + dp[i-list[j]]) % 10007;
        }
    }

    cout<<dp[n];

    return 0;
}
