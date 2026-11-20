#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool dfs(
    const vector<vector<string>>& tickets,
    vector<string>& answer,
    string cur,
    vector<bool>& used
) {
    if(answer.size() == tickets.size() + 1) return true;
    
    for(int i=0; i<tickets.size(); i++){
        if(tickets[i][0] != cur) continue;
        if(used[i]) continue;
        
        used[i] = true;
        answer.push_back(tickets[i][1]);
        if(dfs(tickets, answer, tickets[i][1], used)) return true;
        used[i] = false;
        answer.pop_back();
        
    }
    return false;
}

vector<string> solution(vector<vector<string>> tickets) {
    vector<string> answer;
    
    sort(tickets.begin(), tickets.end());
    answer.push_back("ICN");
    
    int n = tickets.size();
    vector<bool> used(n, false);
    
    dfs(tickets, answer, "ICN", used);
    
    return answer;
}