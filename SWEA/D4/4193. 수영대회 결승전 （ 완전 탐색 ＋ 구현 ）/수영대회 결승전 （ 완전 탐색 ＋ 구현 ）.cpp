#include <iostream>
#include <vector>
#include <queue>

using namespace std;

/*
소용돌이 없는 시간: 2,5,8,... time%3==2
*/

struct Node
{
	int r;
	int c;
	int time;
};

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{

		int n;
		cin >> n;
		bool goal = false;

		vector<vector<int>> grid(n, vector<int>(n));
		vector<vector<bool>> visited(n, vector<bool>(n, false));

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cin >> grid[i][j];
			}
		}

		int sR, sC, eR, eC;
		cin >> sR >> sC >> eR >> eC;

		int dr[4] = { -1,1,0,0 };
		int dc[4] = { 0,0,-1,1 };

		int answer = -1;
		queue<Node> q;
		q.push({ sR, sC, 0 });
		visited[sR][sC] = true;
		
		while (!q.empty()) {

			int r = q.front().r;
			int c = q.front().c;
			int time = q.front().time;
			q.pop();

			if (r == eR && c == eC) {
				goal = true;
				answer = time;
				break;
			}

			for (int d = 0; d < 4; d++) {
				int nr = r + dr[d];
				int nc = c + dc[d];

				if (0 <= nr && nr < n && 0 <= nc && nc < n && !visited[nr][nc] && grid[nr][nc] != 1) {
					if (grid[nr][nc] == 0 ||(grid[nr][nc] == 2 && time % 3 == 2)) {
						visited[nr][nc] = true;
						q.push({ nr, nc, time + 1 });
					}
					else if (grid[nr][nc] == 2 && time % 3 != 2) {
						q.push({ r, c, time + 1 });
					}
				}
			}

		}

		if(goal) cout << "#" << test_case << " " << answer << "\n";
		else cout << "#" << test_case << " " << answer << "\n";

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}