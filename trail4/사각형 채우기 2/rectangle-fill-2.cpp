#include <iostream>

using namespace std;

int n;

int main() {
    cin >> n;

    // Please write your code here.

    // N=1 -> 1
    // N=2 -> 11 2 4 -> 3
    // N=3 -> 111 12 21 14 41 -> 5
    // N=4 -> 1111 112 121 211(x2) 22 24 42 44 -> 11
    // N=5 -> 11111 4x2 3x2x2 -> 21

    // N=4 -> N=3에 한 칸 더함 -> N=1 방법으로 채우기 가능 -> 5 * 1 -> 5
    //     -> N=2에 두 칸 더함 -> 2 또는 4 -> 3 * 2 -> 6

    // dp[i] = dp[i-1] + dp[i-2] * 2

    int dp[n+1] = {};
    dp[1] = 1;
    dp[2] = 3;

    for(int i=3; i<=n; i++){
        dp[i] = (dp[i-1] + dp[i-2] * 2)%10007;
    }

    cout<<dp[n];

    return 0;
}
