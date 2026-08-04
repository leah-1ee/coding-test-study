#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

// 좌상부터 시계방향: 좌상 상 우상 우 우하 하 좌하 좌
int dr[8] = { -1,-1,-1,0,1,1,1,0 };
int dc[8] = { -1,0,1,1,1,0,-1,-1 };

// 8방향 . 인지?
bool isZero(const vector<string>& grid, int r, int c, int n) {
	for (int d = 0; d < 8; d++) {
		int nr = r + dr[d];
		int nc = c + dc[d];
		bool isRange = (0 <= nr && nr < n && 0 <= nc && nc < n);

		if (!isRange) continue;
		if (grid[nr][nc] != '.') return false;
	}

	return true;
}

// 0 주변 8칸 전부 연쇄적으로 열기 
void unlock(
	const vector<string>& grid,
	vector<vector<bool>>& visited,
	int i,
	int j,
	int n
)
{
	int startR = i;
	int startC = j;
	queue<pair<int, int>> q;
	q.emplace(startR, startC);
	visited[startR][startC] = true;

	while (!q.empty()) {
		auto cur = q.front();
		q.pop();

		for (int d = 0; d < 8; d++) {
			int nr = cur.first + dr[d];
			int nc = cur.second + dc[d];

			bool isRange = (0 <= nr && nr < n && 0 <= nc && nc < n);
			if (!isRange || grid[nr][nc] != '.' || visited[nr][nc]) continue;
			visited[nr][nc] = true;

			if(isZero(grid, nr, nc, n)) q.emplace(nr, nc);
			
		}
	}

}

int bfs() {
	int n;
	cin >> n;

	vector<string> grid(n);
	for (int i = 0; i < n; i++) {
		cin >> grid[i];
	}

	int cnt = 0;

	vector<vector<bool>> visited(n, vector<bool>(n, false));
	

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (visited[i][j] || grid[i][j] != '.') continue;
			if (isZero(grid, i, j, n)) {
				unlock(grid, visited, i, j, n);
				cnt++;
			} 
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (!visited[i][j] && grid[i][j] == '.') cnt++;
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

		int cnt = bfs();

		cout << "#" << test_case << " " << cnt << "\n";

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}