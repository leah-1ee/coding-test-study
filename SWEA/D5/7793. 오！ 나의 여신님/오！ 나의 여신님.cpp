#include <iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;

struct Node
{
	int r;
	int c;
	int time;
};

const int dr[4] = { -1,1,0,0 };
const int dc[4] = { 0,0,-1,1 };

void spreadDemon(
	queue<Node>& demon,
	vector<vector<bool>>& hand,
	const vector<string> grid,
	int n,
	int m,
	int curTime
	) 
{
	while (!demon.empty() && demon.front().time == curTime) {
		Node cur = demon.front();
		demon.pop();

		for (int d = 0; d < 4; d++) {
			int nr = cur.r + dr[d];
			int nc = cur.c + dc[d];

			bool inRange = (0 <= nr && nr < n && 0 <= nc && nc < m);
			if (!inRange || hand[nr][nc]) continue;
			if (grid[nr][nc] != '.' && grid[nr][nc] != 'S') continue;
			
			hand[nr][nc] = true;
			demon.push({ nr, nc, curTime + 1 });
		}
	}
}

int bfs() {
	int n, m;
	cin >> n >> m;

	vector<string> grid(n);
	for (int i = 0; i < n; i++) {
		cin >> grid[i];
	}

	int startR = -1, startC = -1, endR = -1, endC = -1;
	vector<vector<bool>> visited(n, vector<bool>(m, false));
	vector<vector<bool>> hand(n, vector<bool>(m, false));

	queue<Node> demon;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (grid[i][j] == 'S') {
				startR = i;
				startC = j;
			}
			if (grid[i][j] == 'D') {
				endR = i;
				endC = j;
			}
			if (grid[i][j] == '*') {
				demon.push({ i,j,0 });
				hand[i][j] = true;
			}
		}
	}

	queue<Node> q;
	q.push({ startR, startC, 0 });
	visited[startR][startC] = true;

	while (!q.empty()) {
		Node cur = q.front();
		q.pop();

		spreadDemon(demon, hand, grid, n, m, cur.time);

		if (cur.r == endR && cur.c == endC) {
			return cur.time;
		}

		for (int d = 0; d < 4; d++) {
			int nr = cur.r + dr[d];
			int nc = cur.c + dc[d];

			bool inRange = (0 <= nr && nr < n && 0 <= nc && nc < m);
			if (!inRange || visited[nr][nc] || hand[nr][nc]) continue; 
			if (grid[nr][nc] != '.' && grid[nr][nc] != 'D') continue;
			visited[nr][nc] = true;
			q.push({ nr, nc, cur.time + 1 });
		}
	}

	return -1;
}

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin >> T;
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		int answer = bfs();

		if (answer >= 0) cout << "#" << test_case << " " << answer <<"\n";
		else cout << "#" << test_case << " GAME OVER\n";

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}