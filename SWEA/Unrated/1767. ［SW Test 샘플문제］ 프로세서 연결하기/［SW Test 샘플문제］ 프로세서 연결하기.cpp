#include <iostream>
#include <vector>
 
using namespace std;

vector<pair<int, int>> cores;
int core = 0, len = 0;

void dfs(
	vector<vector<bool>>& visited,
	int n,
	int curCore,
	int curLen,
	int idx
) {
	// 가지치기 core
	if (curCore + (cores.size() - idx) < core) return;

	// 가지치기 len 
	if ((curCore + (cores.size() - idx) == core) && curLen > len) return;

	// 종료조건 
	if (idx == cores.size()) {
		if (curCore > core) {
			core = curCore;
			len = curLen;
		}
		if (curCore == core && curLen < len) len = curLen;
		return;
	}

	int r = cores[idx].first;
	int c = cores[idx].second;

	// top r
	int top = r;
	bool flag = true;

	for (int i = 1; i <= top; i++) {
		if (visited[r - i][c] == true) {
			flag = false;
			break;
		}
	}
	if (flag) {
		for (int i = 1; i <= top; i++) {
			visited[r - i][c] = true;
		}
		dfs(visited, n, curCore + 1, curLen + top, idx + 1);
		for (int i = 1; i <= top; i++) {
			visited[r - i][c] = false;
		}
	}


	// left c
	int left = c;
	flag = true;

	for (int i = 1; i <= left; i++) {
		if (visited[r][c - i] == true) {
			flag = false;
			break;
		}
	}
	if (flag) {
		for (int i = 1; i <= left; i++) {
			visited[r][c - i] = true;
		}
		dfs(visited, n, curCore + 1, curLen + left, idx + 1);
		for (int i = 1; i <= left; i++) {
			visited[r][c - i] = false;
		}
	}

	// bottom n - 1 - r
	int bottom = n - 1 - r;
	flag = true;

	for (int i = 1; i <= bottom; i++) {
		if (visited[r + i][c] == true) {
			flag = false;
			break;
		}
	}
	if (flag) {
		for (int i = 1; i <= bottom; i++) {
			visited[r + i][c] = true;
		}
		dfs(visited, n, curCore + 1, curLen + bottom, idx + 1);
		for (int i = 1; i <= bottom; i++) {
			visited[r + i][c] = false;
		}
	}

	// right n - 1 - c
	int right = n - 1 - c;
	flag = true;

	for (int i = 1; i <= right; i++) {
		if (visited[r][c + i] == true) {
			flag = false;
			break;
		}
	}
	if (flag) {
		for (int i = 1; i <= right; i++) {
			visited[r][c + i] = true;
		}
		dfs(visited, n, curCore + 1, curLen + right, idx + 1);
		for (int i = 1; i <= right; i++) {
			visited[r][c + i] = false;
		}
	}

	// x
	dfs(visited, n, curCore, curLen, idx + 1);
}

int main(int argc, char** argv)
{
	int test_case;
	int T;
	
	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{

		core = 0;
		len = 0;
		cores.clear();

		int n;
		cin >> n;

		vector<vector<int>> grid(n, vector<int>(n));

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cin >> grid[i][j];
			}
		}

		vector<vector<bool>> visited(n, vector<bool>(n, false));

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (grid[i][j] == 1) {
					visited[i][j] = true;
					if (i == 0 || i == n - 1 || j == 0 || j == n - 1) core++;
					else cores.push_back({ i,j });
				}
			}
		}

		dfs(visited, n, core, 0, 0);

		cout << "#" << test_case << " " << len << "\n";

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}