#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    
    int score[3] = {0};
    
    int answer1[5] = {1,2,3,4,5};
    int answer2[8] = {2, 1, 2, 3, 2, 4, 2, 5};
    int answer3[10] = {3,3,1,1,2,2,4,4,5,5};
    
    for(int i=0; i<answers.size(); i++){
        if(answer1[i%5] == answers[i]) score[0]++;
        
        if(i==0 && answers[0] == 2) score[1]++;
        else if(answer2[i%8] == answers[i]) score[1]++;
        
        if(answer3[i%10] == answers[i]) score[2]++;
    }
    
    int maxScore = 0;
    for(int i=0; i<3; i++){
        maxScore = max(maxScore, score[i]);
    }
    
    for(int i=0; i<3; i++){
        if(score[i] == maxScore) answer.push_back(i+1);
    }
    
    return answer;
}