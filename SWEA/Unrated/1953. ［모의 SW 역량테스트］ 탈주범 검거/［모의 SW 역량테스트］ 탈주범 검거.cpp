#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Node
{
	int r;
	int c;
	int time;
};

// 상하좌우
int dr[4] = { -1,1,0,0 };
int dc[4] = { 0,0,-1,1 };

int bfs() {
	int n, m, startR, startC, L;
	cin >> n >> m >> startR >> startC >> L;

	vector<vector<int>> grid(n, vector<int>(m));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> grid[i][j];
		}
	}

	queue<Node> q;
	q.push({ startR, startC, 1 });

	vector<vector<bool>> visited(n, vector<bool>(m, false));
	visited[startR][startC] = true;

	int cnt = 1;

	while (!q.empty()) {
		int r = q.front().r;
		int c = q.front().c;
		int t = q.front().time;
		q.pop();

		// cout << r << " " << c << " " << t << "\n";

		int type = grid[r][c];

		if (t == L) break;

		if (type == 0) continue;

		int nr, nc;

		// 상하좌우
		if (type == 1) {
			for (int d = 0; d < 4; d++) {
				nr = r + dr[d];
				nc = c + dc[d];

				bool isRange = (0 <= nr && nr < n && 0 <= nc && nc < m);
				if (isRange  && !visited[nr][nc]) {
					int ntype = grid[nr][nc];
					if (ntype == 0) continue;

					if (d == 0 && !(ntype == 1 || ntype == 2 || ntype == 5 || ntype == 6)) continue;
					if (d == 1 && !(ntype == 1 || ntype == 2 || ntype == 4 || ntype == 7)) continue;
					if (d == 2 && !(ntype == 1 || ntype == 3 || ntype == 4 || ntype == 5)) continue;
					if (d == 3 && !(ntype == 1 || ntype == 3 || ntype == 6 || ntype == 7)) continue;

					cnt++;
					q.push({ nr, nc, t + 1 });
					visited[nr][nc] = true;
				}
			}
		}
		// 상하 01
		else if (type == 2) {
			for (int d = 0; d < 2; d++) {
				nr = r + dr[d];
				nc = c + dc[d];

				bool isRange = (0 <= nr && nr < n && 0 <= nc && nc < m);
				if (isRange  && !visited[nr][nc]) {
					int ntype = grid[nr][nc];
					if (ntype == 0) continue;

					if (d == 0 && !(ntype == 1 || ntype == 2 || ntype == 5 || ntype == 6)) continue;
					if (d == 1 && !(ntype == 1 || ntype == 2 || ntype == 4 || ntype == 7)) continue;
					if (d == 2 && !(ntype == 1 || ntype == 3 || ntype == 4 || ntype == 5)) continue;
					if (d == 3 && !(ntype == 1 || ntype == 3 || ntype == 6 || ntype == 7)) continue;


					cnt++;
					q.push({ nr, nc, t + 1 });
					visited[nr][nc] = true;
				}
			}
		}

		// 좌우 23
		else if (type == 3) {
			for (int d = 2; d < 4; d++) {
				nr = r + dr[d];
				nc = c + dc[d];

				bool isRange = (0 <= nr && nr < n && 0 <= nc && nc < m);
				if (isRange  && !visited[nr][nc]) {
					int ntype = grid[nr][nc];
					if (ntype == 0) continue;

					if (d == 0 && !(ntype == 1 || ntype == 2 || ntype == 5 || ntype == 6)) continue;
					if (d == 1 && !(ntype == 1 || ntype == 2 || ntype == 4 || ntype == 7)) continue;
					if (d == 2 && !(ntype == 1 || ntype == 3 || ntype == 4 || ntype == 5)) continue;
					if (d == 3 && !(ntype == 1 || ntype == 3 || ntype == 6 || ntype == 7)) continue;

					cnt++;
					q.push({ nr, nc, t + 1 });
					visited[nr][nc] = true;
				}
			}
		}

		// 상우 03
		else if (type == 4) {
			for (int d = 0; d < 4; d += 3) {
				nr = r + dr[d];
				nc = c + dc[d];

				bool isRange = (0 <= nr && nr < n && 0 <= nc && nc < m);
				if (isRange  && !visited[nr][nc]) {
					int ntype = grid[nr][nc];
					if (ntype == 0) continue;

					if (d == 0 && !(ntype == 1 || ntype == 2 || ntype == 5 || ntype == 6)) continue;
					if (d == 1 && !(ntype == 1 || ntype == 2 || ntype == 4 || ntype == 7)) continue;
					if (d == 2 && !(ntype == 1 || ntype == 3 || ntype == 4 || ntype == 5)) continue;
					if (d == 3 && !(ntype == 1 || ntype == 3 || ntype == 6 || ntype == 7)) continue;

					cnt++;
					q.push({ nr, nc, t + 1 });
					visited[nr][nc] = true;
				}
			}
		}

		// 하우 13
		else if (type == 5) {
			for (int d = 1; d < 4; d+=2) {
				nr = r + dr[d];
				nc = c + dc[d];

				bool isRange = (0 <= nr && nr < n && 0 <= nc && nc < m);
				if (isRange  && !visited[nr][nc]) {
					int ntype = grid[nr][nc];
					if (ntype == 0) continue;

					if (d == 0 && !(ntype == 1 || ntype == 2 || ntype == 5 || ntype == 6)) continue;
					if (d == 1 && !(ntype == 1 || ntype == 2 || ntype == 4 || ntype == 7)) continue;
					if (d == 2 && !(ntype == 1 || ntype == 3 || ntype == 4 || ntype == 5)) continue;
					if (d == 3 && !(ntype == 1 || ntype == 3 || ntype == 6 || ntype == 7)) continue;

					cnt++;
					q.push({ nr, nc, t + 1 });
					visited[nr][nc] = true;
				}
			}
		}

		// 하좌 12
		else if (type == 6) {
			for (int d = 1; d < 3; d++) {
				nr = r + dr[d];
				nc = c + dc[d];

				bool isRange = (0 <= nr && nr < n && 0 <= nc && nc < m);
				if (isRange  && !visited[nr][nc]) {
					int ntype = grid[nr][nc];
					if (ntype == 0) continue;

					if (d == 0 && !(ntype == 1 || ntype == 2 || ntype == 5 || ntype == 6)) continue;
					if (d == 1 && !(ntype == 1 || ntype == 2 || ntype == 4 || ntype == 7)) continue;
					if (d == 2 && !(ntype == 1 || ntype == 3 || ntype == 4 || ntype == 5)) continue;
					if (d == 3 && !(ntype == 1 || ntype == 3 || ntype == 6 || ntype == 7)) continue;

					cnt++;
					q.push({ nr, nc, t + 1 });
					visited[nr][nc] = true;
				}
			}
		}

		// 상좌 02
		else if (type == 7) {
			for (int d = 0; d < 4; d+=2) {
				nr = r + dr[d];
				nc = c + dc[d];

				bool isRange = (0 <= nr && nr < n && 0 <= nc && nc < m);
				if (isRange  && !visited[nr][nc]) {
					int ntype = grid[nr][nc];
					if (ntype == 0) continue;

					if (d == 0 && !(ntype == 1 || ntype == 2 || ntype == 5 || ntype == 6)) continue;
					if (d == 1 && !(ntype == 1 || ntype == 2 || ntype == 4 || ntype == 7)) continue;
					if (d == 2 && !(ntype == 1 || ntype == 3 || ntype == 4 || ntype == 5)) continue;
					if (d == 3 && !(ntype == 1 || ntype == 3 || ntype == 6 || ntype == 7)) continue;

					cnt++;
					q.push({ nr, nc, t + 1 });
					visited[nr][nc] = true;
				}
			}
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

		cout << "#" << test_case << " " << bfs() << "\n";

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}