#include <iostream>
#include <cmath>

using namespace std;

int n;

int main() {
    cin >> n;

    // Please write your code here.

    // N을 1과 2로 구성, 블럭당 경우의 수 2개
    // N=1 -> 1 -> 2
    // N=2 -> 11(4) 2(4) 중복1 -> 7
    // N=3 -> 111(8) 12(8) 21(8) 중복2 -> 22
    // N=4 -> 1111(16) 211(8) 121(8) 112(8) 22(4) 중복 4 -> 71
    // N=5 -> 11111(32) 2111 1211 1121 1112(16) 221 212 122(8) 중복 7 -> 228

    // 마지막 세로 2칸 채운다: 경우의 수 2개 -> dp[i-1] * 2
    // 가로 사용: 경우의 수 3개 -> dp[i-2] * 3

    long long dp[n+1];
    for(int i=0; i<=n; i++){
        dp[i] = 0;
    }

    dp[0] = 1;
    dp[1] = 2;

    for(int i=2; i<=n; i++){
        dp[i] = (dp[i-1] * 2 + dp[i-2] * 3) % 1000000007;
        for(int j=i-3; j>=0; j--){
            dp[i] = (dp[i] + dp[j] * 2) % 1000000007;
        }
    }

    cout << dp[n];

    return 0;
}
