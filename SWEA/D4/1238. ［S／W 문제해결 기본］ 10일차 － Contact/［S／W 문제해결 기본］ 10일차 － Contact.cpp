#include<iostream>
#include <vector>
#include <queue>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T = 10;

	for (test_case = 1; test_case <= T; ++test_case)
	{

		int n, start;
		cin >> n >> start;

		vector<vector<int>> graph(101);
		vector<bool> visited(101, false);

		for (int i = 0; i < n/2; i++) {
			int from, to;
			cin >> from >> to;
			graph[from].push_back(to);
		}

		queue<int> q;
		q.push(start);
		visited[start] = true;

		int answer;

		while (!q.empty()) {
			int last = 0;
			int size = q.size();
			for (int i = 0; i < size; i++) {
				int cur = q.front();
				q.pop();

				if (cur > last) last = cur;

				for (int next : graph[cur]) {
					if (!visited[next]) {
						visited[next] = true;
						q.push(next);
					}
				}
			}
			answer = last;
		}

		cout << "#" << test_case << " " << answer << "\n";

	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}