#include <iostream>
#include <vector>
using namespace std;

int dr[4] = { -1, 0, 1, 0 };
int dc[4] = { 0, 1, 0,-1 };


// 하나의 미생물 군집 정보를 저장하는 구조체
struct Group {

	int r;      // 현재 행 위치
	int c;      // 현재 열 위치

	int cnt;    // 미생물 수

	int dir;    
};


int main() {


	ios::sync_with_stdio(false);
	cin.tie(NULL);


	// 테스트 케이스 개수
	int T;
	cin >> T;


	// tc = 현재 테스트 케이스 번호
	for (int tc = 1; tc <= T; tc++) {

		int N;  // 맵 크기
		int M;  // 격리 시간
		int K;  // 최초 미생물 군집 개수

		cin >> N >> M >> K;


		// 현재 존재하는 모든 미생물 군집 저장
		vector<Group> groups;


		// K개의 초기 군집 입력
		for (int i = 0; i < K; i++) {

			int r, c, cnt, d;

			cin >> r >> c >> cnt >> d;




			if (d == 1)
				d = 0; 

			else if (d == 4)
				d = 1; 

			groups.push_back({ r, c, cnt, d });
		}

		for (int time = 0; time < M; time++) {

			vector<vector<int>> board(
				N,
				vector<int>(N, -1)
			);


			vector<vector<int>> maxCnt(
				N,
				vector<int>(N, 0)
			);


			vector<Group> nextGroups;


			// 현재 존재하는 모든 군집을 하나씩 이동
			for (Group cur : groups) {


				int nr = cur.r + dr[cur.dir];
				int nc = cur.c + dc[cur.dir];


				// 이동한 군집의 미생물 수
				int cnt = cur.cnt;

				// 이동한 군집의 방향
				int dir = cur.dir;


				if (nr == 0 || nr == N - 1 ||
					nc == 0 || nc == N - 1) {



					cnt /= 2;

					dir = (dir + 2) % 4;
				}



				if (cnt == 0)
					continue;




				if (board[nr][nc] == -1) {


	
					int idx = nextGroups.size();


					// 새로운 군집 추가
					nextGroups.push_back({
						nr,
						nc,
						cnt,
						dir
						});


					// 이 좌표에 저장된 군집은
					// nextGroups[idx]라고 기록
					board[nr][nc] = idx;


					// 현재까지 이 칸에 온 가장 큰 군집은
					// 당연히 지금 이 군집
					maxCnt[nr][nc] = cnt;
				}


				else {


					// 이 위치의 군집이
					// nextGroups 몇 번째에 저장됐는지 가져옴
					int idx = board[nr][nc];


					nextGroups[idx].cnt += cnt;




					if (cnt > maxCnt[nr][nc]) {


						// 지금 들어온 군집이 더 크다면
						// 최대 크기 갱신
						maxCnt[nr][nc] = cnt;


						// 방향도 지금 군집의 방향으로 변경
						nextGroups[idx].dir = dir;
					}
				}
			}



			groups = nextGroups;
		}




		int answer = 0;


		// 현재 남아 있는 모든 군집의 미생물 수 합산
		for (Group g : groups) {
			answer += g.cnt;
		}


		// 정답 출력
		cout << "#" << tc << " " << answer << '\n';
	}


	return 0;
}