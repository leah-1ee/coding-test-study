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

void demonHand(
	vector<string>& grid,
	queue<Node>& demon,
	int t,
	int n,
	int m
) {
	while (!demon.empty()) {
		Node cur = demon.front();
		
		if (cur.time != t)
			return;

		demon.pop();

		for (int d = 0; d < 4; d++) {
			int nr = cur.r + dr[d];
			int nc = cur.c + dc[d];

			bool isRange = (0 <= nr && nr < n && 0 <= nc && nc < m);
			if (isRange && (grid[nr][nc] == '.' || grid[nr][nc] == 'S')) {
				grid[nr][nc] = '*';
				demon.push({ nr,nc,cur.time + 1 });
			}
		}
	}
}

int bfs() {
	int n, m;
	cin >> n >> m;

	vector<string> grid(n);
	int sr, sc, er, ec;

	queue<Node> demon;

	for (int i = 0; i < n; i++) {
		cin >> grid[i];
		for (int j = 0; j < m; j++) {
			
			if (grid[i][j] == 'S') {
				sr = i; sc = j;
			}
			if (grid[i][j] == 'D') {
				er = i; ec = j;
			}
			if (grid[i][j] == '*') {
				demon.push({ i,j,0 });
			}
		}
	}

	queue<Node> q;
	q.push({ sr,sc,0 });

	vector<vector<bool>> visited(n, vector<bool>(m, false));
	visited[sr][sc] = true;

	while (!q.empty()) {
		Node cur = q.front();
		q.pop();

		if (cur.r == er && cur.c == ec)
			return cur.time;

		demonHand(grid, demon, cur.time, n, m);

		for (int d = 0; d < 4; d++) {
			int nr = cur.r + dr[d];
			int nc = cur.c + dc[d];

			bool isRange = (0 <= nr && nr < n && 0 <= nc && nc < m);
			if (isRange && !visited[nr][nc] && (grid[nr][nc] == '.' || grid[nr][nc] == 'D')) {
				visited[nr][nc] = true;
				q.push({ nr,nc,cur.time + 1 });
			}
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

		if (answer >= 0) cout << "#" << test_case << " " << answer << "\n";
		else cout << "#" << test_case << " GAME OVER\n";

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}