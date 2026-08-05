#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <climits>
#include <tuple>
#include <functional>

using namespace std;

int dr[4] = { -1,1,0,0 };
int dc[4] = { 0,0,-1,1 };

int solve() {
	int n;
	cin >> n;

	vector<string> raw(n);
	for (int i = 0; i < n; i++) {
		cin >> raw[i];
	}

	vector<vector<int>> grid(n, vector<int>(n));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			grid[i][j] = raw[i][j] - '0';
		}
	}

	vector<vector<int>> dist(n, vector<int>(n, INT_MAX));

	priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<>> pq;

	dist[0][0] = 0;
	pq.push({ 0,0,0 });

	while (!pq.empty()) {
		auto[d, r, c] = pq.top(); pq.pop();

		if (d > dist[r][c]) continue;

		if (r == n - 1 && c == n - 1) break;

		for (int dir = 0; dir < 4; dir++) {
			int nr = r + dr[dir];
			int nc = c + dc[dir];

			if (nr<0 || nr>=n || nc<0 || nc>=n) continue;

			int ncost = d + grid[nr][nc];
			if (ncost < dist[nr][nc]) {
				dist[nr][nc] = ncost;
				pq.push({ ncost,nr,nc });
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