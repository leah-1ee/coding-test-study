#include <iostream>

using namespace std;

int n, k;
int arr[1001];

int main() {
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Please write your code here.
    int prefix[1002] = {};

    // 누적합 배열 만들기
    for(int i=1; i<=n; i++){
        prefix[i] = prefix[i-1] + arr[i];
    }

    int cnt = 0;

    // 합 K인지 검사
    for(int i=1; i<=n; i++){
        for(int j=0; j<i; j++){
            if((prefix[i] - prefix[j]) == k) cnt++;
        }
    }

    cout<<cnt;

    return 0;
}
