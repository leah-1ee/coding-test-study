#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// 방향: 0=상,1=하,2=좌,3=우
const int dr[4] = { -1, 1, 0, 0 };
const int dc[4] = { 0, 0, -1, 1 };

enum Dir { UP = 1, DOWN = 2, LEFT = 4, RIGHT = 8 };
const int dirBit[4] = { UP, DOWN, LEFT, RIGHT };
const int oppBit[4] = { DOWN, UP, RIGHT, LEFT }; // 이웃이 나와 연결되려면 반대 방향이 열려있어야 함

// 파이프 타입별 연결 방향 (0번 인덱스는 사용 안 함: type 0 = 벽)
const int connMask[8] = {
	0,                    // 0: 벽
	UP | DOWN | LEFT | RIGHT, // 1: 십자
	UP | DOWN,            // 2: 상하
	LEFT | RIGHT,         // 3: 좌우
	UP | RIGHT,           // 4: 상우
	DOWN | RIGHT,         // 5: 하우
	DOWN | LEFT,          // 6: 하좌
	UP | LEFT             // 7: 상좌
};

struct Node { int r, c, time; };

int bfs() {
	int n, m, startR, startC, L;
	cin >> n >> m >> startR >> startC >> L;

	vector<vector<int>> grid(n, vector<int>(m));
	for (auto& row : grid)
		for (auto& v : row) cin >> v;

	vector<vector<bool>> visited(n, vector<bool>(m, false));
	queue<Node> q;
	q.push({ startR, startC, 1 });
	visited[startR][startC] = true;
	int cnt = 1;

	while (!q.empty()) {
		auto[r, c, t] = q.front(); q.pop();
		if (t == L) break;

		int curMask = connMask[grid[r][c]];
		if (curMask == 0) continue;

		for (int d = 0; d < 4; d++) {
			if (!(curMask & dirBit[d])) continue; // 현재 타입이 이 방향으로 안 열림

			int nr = r + dr[d], nc = c + dc[d];
			if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
			if (visited[nr][nc]) continue;

			int ntype = grid[nr][nc];
			if (!(connMask[ntype] & oppBit[d])) continue; // 이웃이 반대 방향으로 안 열림

			visited[nr][nc] = true;
			cnt++;
			q.push({ nr, nc, t + 1 });
		}
	}
	return cnt;
}

int main() {
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++)
		cout << "#" << tc << " " << bfs() << "\n";
	return 0;
}