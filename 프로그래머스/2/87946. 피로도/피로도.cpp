#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int k, vector<vector<int>> dungeons) {
    
    sort(dungeons.begin(), dungeons.end());
    int health = k;
    int maxCnt = 0;
    do{
        health = k;
        int cnt = 0;
        for(int i=0; i<dungeons.size(); i++){
            if(health >= dungeons[i][0]) {
                health -= dungeons[i][1];
                cnt++;
            }
        }
        maxCnt = max(maxCnt, cnt);
    } while(next_permutation(dungeons.begin(), dungeons.end()));
    
    return maxCnt;
}