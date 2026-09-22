#include <iostream>
#include <algorithm>

using namespace std;

int n, k;
int arr[100002];

int main() {
    cin >> n >> k;
    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
    }

    // Please write your code here.

    // 누적합 만들기
    int prefix_sum[100002] = {};
    for(int i=1; i<=n; i++)
        prefix_sum[i] = prefix_sum[i-1] + arr[i];

    // K 개 유지, 이동하면서 빼기, 최댓값 업데이트
    int maxVal = -1e9;
    for(int i=0; i<n-k; i++){
        int sumK = prefix_sum[i+k] - prefix_sum[i];
        maxVal = max(maxVal, sumK);
    }

    cout<<maxVal;

    return 0;
}
