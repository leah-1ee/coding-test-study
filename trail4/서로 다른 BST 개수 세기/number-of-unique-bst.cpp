#include <iostream>

using namespace std;

int n;

int main() {
    cin >> n;

    // Please write your code here.

    // N=1 -> 1
    // N=2 -> 2
    // N=3 -> 2 1 2 -> 5
    // N=4 -> 5 2 2 5 -> 14
    // N=5 -> 0/4  1/3  2/2 3/1  4/0 -> 14 5 4 5 14 -> 42
    // N=6 -> 0/5 1/4 2/3 3/2 4/1 5/0 -> 42 14 10 10 14 42 -> 132

    // left * right 꼴
    // 

    long long dp[n+1] = {};
    dp[0] = 1;

    for(int i=1; i<=n; i++){
        for(int left = 0; left < i; left++){
            int right = i - 1 - left;
            dp[i] += dp[left] * dp[right];
        }
    }

    cout<<dp[n];

    return 0;
}
