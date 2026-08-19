#include <iostream>
#include <vector>

using namespace std;
vector<vector<bool>> visited;
vector<pair<int, int>> cores;
int bestCore, bestLen, n;

int dr[4] = { -1,1,0,0 };
int dc[4] = { 0,0,-1,1 };

bool canPlace(int dist, int r, int c, int d) {
	for (int i = 1; i <= dist; i++) {
		if (visited[r + dr[d] * i][c + dc[d] * i]) return false;
	}
	return true;
}

void Place(int dist, int r, int c, int d, bool flag) {
	for (int i = 1; i <= dist; i++) {
		visited[r + dr[d] * i][c + dc[d] * i] = flag;
	}
}

void dfs(int curCore, int curLen, int idx) {
	int remain = cores.size() - idx;
	if (curCore + remain < bestCore) return;
	if (curCore + remain == bestCore && curLen > bestLen) return;

	if (idx == cores.size()) {
		if (curCore > bestCore || (curCore == bestCore && curLen < bestLen)) {
			bestCore = curCore;
			bestLen = curLen;
		}
		return;
	}


	auto[r, c] = cores[idx];

	// 상하좌우 길이
	int dist[4] = { r, n - 1 - r, c, n - 1 - c };

	for (int d = 0; d < 4; d++) {
			
		if (canPlace(dist[d], r, c, d)) {
			Place(dist[d], r, c, d, true);
			dfs(curCore + 1, curLen + dist[d], idx+1);
			Place(dist[d], r, c, d, false);
		}
	}

	dfs(curCore, curLen, idx + 1);

}

int main() {
	int T; cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cin >> n;

		vector<vector<int>> grid(n, vector<int>(n));
		for (auto& row : grid) for (auto& v : row) cin >> v;

		visited.assign(n, vector<bool>(n, false));
		cores.clear();

		int sideCore = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (grid[i][j] == 1) {
					visited[i][j] = true;
					if (i == 0 || i == n - 1 || j == 0 || j == n - 1) {
						sideCore++;
					}
					else cores.push_back({ i, j });
				}
			}
		}
		bestCore = sideCore;
		bestLen = 0;

		dfs(sideCore, 0, 0);

		cout << "#" << tc << " " << bestLen << "\n";

	}
}