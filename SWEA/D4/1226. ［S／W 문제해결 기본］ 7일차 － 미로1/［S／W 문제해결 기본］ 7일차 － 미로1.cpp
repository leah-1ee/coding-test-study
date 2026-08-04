#include<iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T = 10;

	/*
	   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
	*/
	for (test_case = 1; test_case <= T; ++test_case)
	{
		int a;
		cin >> a;
		vector<string> grid(16);
		vector<vector<bool>> visited(16, vector<bool>(16, false));
		bool found = false;

		for (int i = 0; i < 16; i++) {
			cin >> grid[i];
		}

		int startR, startC, endR, endC;

		for (int i = 0; i < 16; i++) {
			for (int j = 0; j < 16; j++) {
				if (grid[i][j] == '2') {
					startR = i; startC = j;
				}
				if (grid[i][j] == '3') {
					endR = i; endC = j;
				}
			}
		}

		int dr[4] = { -1,1,0,0 };
		int dc[4] = { 0,0,-1,1 };

		queue<pair<int, int>> q;
		q.emplace(startR, startC);
		visited[startR][startC] = true;

		while (!q.empty()) {
			int r = q.front().first;
			int c = q.front().second;
			q.pop();

			if (r == endR && c == endC) {
				found = true;
				break;
			}

			for (int d = 0; d < 4; d++) {
				int nr = r + dr[d];
				int nc = c + dc[d];

				if (0 <= nr && nr < 16 && 0 <= nc && nc < 16 && grid[nr][nc] != '1' && !visited[nr][nc]) {
					visited[nr][nc] = true;
					q.emplace(nr, nc);
				}
			}

		}

		if(found) cout << "#" << test_case << " 1\n";
		else cout << "#" << test_case << " 0\n";
		

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
