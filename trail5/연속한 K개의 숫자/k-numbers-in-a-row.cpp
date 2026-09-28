#include <iostream>
#include <algorithm>

using namespace std;

int N, K, B;
int missing[100001];
int miss[100001] = {};

int main() {
    cin >> N >> K >> B;

    for (int i = 0; i < B; i++) {
        cin >> missing[i];
        miss[missing[i]] = 1;
    }

    // Please write your code here.
    int prefix[100001] = {};

    for(int i=1; i<=N; i++){
        prefix[i] = prefix[i-1] + miss[i];
    }

    int least = B;

    for(int i=K; i<=N; i++){
        least = min(least, prefix[i] - prefix[i-K]);
    }

    cout<<least;

    return 0;
}
