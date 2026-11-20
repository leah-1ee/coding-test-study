#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool dfs(
    const vector<vector<string>>& tickets,
    string cur,
    vector<bool>& visited,
    vector<string>& answer
){
    if(answer.size() == tickets.size() + 1) return true;
    
    for(int i=0; i<tickets.size(); i++){
        if(visited[i]) continue;
        if(tickets[i][0] != cur) continue;
        
        visited[i] = true;
        answer.push_back(tickets[i][1]);
        if(dfs(tickets, tickets[i][1], visited, answer)) return true;
        visited[i] = false;
        answer.pop_back();
    }
    
    return false;
}

vector<string> solution(vector<vector<string>> tickets) {
    vector<string> answer;
    answer.push_back("ICN");
    
    sort(tickets.begin(), tickets.end());
    
    int n = tickets.size();
    vector<bool> visited(n, false);
    
    dfs(tickets, "ICN", visited, answer);
    
    return answer;
}