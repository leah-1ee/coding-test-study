#include<iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int n, start;
vector<vector<bool>> graph;

int bfs() {
	queue<int> q;
	q.push(start);

	vector<bool> visited(101, false);
	visited[start] = true;

	int last;

	while (!q.empty()) {
		last = 0;
		int size = q.size();

		for (int i = 0; i < size; i++) {
			
			int num = q.front();
			last = max(last, num);
			q.pop();

			for (int j = 0; j < 101; j++) {
				if (graph[num][j] && !visited[j]) {
					q.push(j);
					visited[j] = true;
				}
			}
		}
	}

	return last;
}

int main(int argc, char** argv)
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int test_case;
	int T = 10;

	for (test_case = 1; test_case <= T; ++test_case)
	{
		graph.assign(101, vector<bool>(101, false));
		cin >> n >> start;
		
		for (int i = 0; i < n/2; i++) {
			int a, b;
			cin >> a >> b;
			graph[a][b] = true;
		}

		int answer = bfs();

		cout << "#" << test_case << " " << answer << "\n";

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}