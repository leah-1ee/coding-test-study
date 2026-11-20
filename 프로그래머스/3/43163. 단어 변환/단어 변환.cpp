#include <string>
#include <vector>
#include <queue>

using namespace std;

bool canChange(string a, string b){
    int diff = 0;
    for(int i=0; i<a.size(); i++){
        if(a[i] != b[i]) diff++;
    }
    return diff==1;
}

int bfs(string begin, string target, const vector<string>& words){
    int n = words.size();
    vector<bool> visited(n, false);
    
    queue<pair<string, int>> q;
    q.push({begin, 0});
    
    while(!q.empty()){
        auto [cur, len] = q.front(); q.pop();
        if(cur == target) return len;
        
        for(int i=0; i<n; i++){
            if(visited[i]) continue;
            if(!canChange(cur, words[i])) continue;
            visited[i] = true;
            q.push({words[i], len+1});
        }
    }
    
    return 0;
}

int solution(string begin, string target, vector<string> words) {
    return bfs(begin, target, words);
}