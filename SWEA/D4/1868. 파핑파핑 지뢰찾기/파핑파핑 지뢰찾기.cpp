#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

// 상하좌우 좌상 우상 우하 좌하
int dr[8] = { -1,1,0,0,-1,-1,1,1 };
int dc[8] = { 0,0,-1,1,-1,1,1,-1 };

bool isZero(const vector<string>& grid, int r, int c, int n) {
	for (int d = 0; d < 8; d++) {
		int nr = r + dr[d];
		int nc = c + dc[d];

		bool isRange = (0 <= nr && nr < n && 0 <= nc && nc < n);
		if (!isRange) continue;
		if (grid[nr][nc] == '*')
			return false;
	}

	return true;
}

void bfs(
	const vector<string>& grid,
	queue<pair<int, int>>& q,
	vector<vector<bool>>& visited,
	int n
) {	

	while (!q.empty()) {
		int r = q.front().first;
		int c = q.front().second;
		q.pop();

		for (int d = 0; d < 8; d++) {
			int nr = r + dr[d];
			int nc = c + dc[d];

			bool isRange = (0 <= nr && nr < n && 0 <= nc && nc < n);
			if (isRange && !visited[nr][nc] && grid[nr][nc] == '.') {
				visited[nr][nc] = true;
				if (isZero(grid, nr, nc, n)) {
					q.push({ nr, nc });
				}
			}	
		}
	}
}

int simulation() {
	int n;
	cin >> n;

	int cnt = 0;
	vector<vector<bool>> visited(n, vector<bool>(n, false));

	vector<string> grid(n);
	for (int i = 0; i < n; i++) {
		cin >> grid[i];
		for (int j = 0; j < n; j++) {
			if (grid[i][j] == '*')
				visited[i][j] = true;
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (!visited[i][j] && grid[i][j] == '.' && isZero(grid, i, j, n)) {

				cnt++;
				// 큐에 넣고 bfs
				queue<pair<int, int>> q;
				q.push({ i,j });
				visited[i][j] = true;
				// bfs
				bfs(grid, q, visited, n);
			}

		}
	}


	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (!visited[i][j])
				cnt++;
		}
	}

	return cnt;

}

int main(int argc, char** argv)
{
	int test_case;
	int T;

	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{

		int cnt = simulation();

		cout << "#" << test_case << " " << cnt << "\n";

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}