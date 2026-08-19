#include <string>
#include <vector>
#include <queue>
#include <climits>
#include <algorithm>

using namespace std;
vector<vector<pair<int, int>>> graph(201);
const int MAX = INT_MAX;


void Dijkstra(int start, vector<int>& dist) {
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int,int>>> pq;

	pq.push({ 0, start });
	dist[start] = 0;

	while (!pq.empty()) {
		auto[price, node] = pq.top(); pq.pop();
		if (price > dist[node]) continue;

		for (auto next : graph[node]) {
			int nextNode = next.first;
			int nextPrice = next.second + price;

			if (nextPrice < dist[nextNode]) {
				dist[nextNode] = nextPrice;
				pq.push({ nextPrice, nextNode });
			}
		}
	}
}

int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
	int answer = MAX;
	
	for (auto & fare : fares) {
		graph[fare[0]].push_back({ fare[1], fare[2] });
		graph[fare[1]].push_back({ fare[0], fare[2] });
	}

	vector<int> distS(201, MAX);
	Dijkstra(s, distS);
	vector<int> distA(201, MAX);
	Dijkstra(a, distA);
	vector<int> distB(201, MAX);
	Dijkstra(b, distB);

	for (int i = 0; i < 201; i++) {
		if (distS[i] == MAX || distA[i] == MAX || distB[i] == MAX) continue;
		answer = min(answer, distS[i] + distA[i] + distB[i]);
	}


	return answer;
}