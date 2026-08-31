#include <iostream>
#include <climits>
#include <queue>
#include <vector>

using namespace std;

int n, m;
int from[1001], to[1001], weight[1001];

int main() {
    cin >> n >> m;

    for (int i = 0; i < m; i++) {
        cin >> from[i] >> to[i] >> weight[i];
    }

    // Please write your code here.
    vector<vector<pair<int, int>>> graph(n+1);
    for(int i=0; i<m; i++){
        int r = from[i];
        int c = to[i];
        int val = weight[i];
        graph[r].push_back({c, val});
    }


    vector<int> dist(n+1, INT_MAX);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    dist[1] = 0;
    pq.push({0,1});

    while(!pq.empty()){
        int val = pq.top().first;
        int node = pq.top().second;
        pq.pop();

        if(val>dist[node]) continue;

        for(auto& next:graph[node]){
            int nextNode = next.first;
            int nextVal = next.second + val;

            if(nextVal<dist[nextNode]){
                dist[nextNode] = nextVal;
                pq.push({nextVal, nextNode});
            }
        }
    }

    for(int i=2; i<=n; i++){
        if(dist[i]==INT_MAX){
            cout<<"-1\n";
        }
        else cout<<dist[i]<<"\n";
    }

    return 0;
}
