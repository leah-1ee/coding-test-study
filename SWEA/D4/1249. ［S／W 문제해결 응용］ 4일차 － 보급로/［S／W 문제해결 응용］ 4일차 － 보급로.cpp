#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <climits>
#include <functional>

using namespace std;

int dr[4] = { -1,1,0,0 };
int dc[4] = { 0,0,-1,1 };

struct Node
{
	int val; int r; int c;
};

struct Compare
{
	bool operator()(const Node& a, const Node& b) const {
		return a.val > b.val;
	}
};

int solve() {
	int n;
	cin >> n;

	vector<string> raw(n);
	for (string &s : raw)
		cin >> s;

	vector<vector<int>> grid(n, vector<int>(n));
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			grid[i][j] = raw[i][j] - '0';

	vector<vector<int>> dist(n, vector<int>(n, INT_MAX));

	priority_queue<Node, vector<Node>, Compare> pq;

	dist[0][0] = 0;
	pq.push({ 0,0,0 });

	while (!pq.empty()) {
		auto[v, r, c] = pq.top();
		pq.pop();

		if (v > dist[r][c]) continue;

		for (int d = 0; d < 4; d++) {
			int nr = r + dr[d];
			int nc = c + dc[d];

			bool isRange = (0 <= nr && nr < n && 0 <= nc && nc < n);
			if (isRange) {
				int newVal = v + grid[nr][nc];
				if (newVal < dist[nr][nc]) {
					dist[nr][nc] = newVal;
					pq.push({ newVal,nr,nc });
				}
			}
		}
	}

	return dist[n - 1][n - 1];
}

int main() {
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cout << "#" << tc << " " << solve() << "\n";
	}

	return 0;
}