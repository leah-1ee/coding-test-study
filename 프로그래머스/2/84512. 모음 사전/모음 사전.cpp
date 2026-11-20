#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string vowels = "AEIOU";
vector<string> words;

void dfs(string cur){
    if(cur.size() == 5) return;
    
    for(char c : vowels) {
        string next = cur + c;
        words.push_back(next);
        dfs(next);
    }
}

int solution(string word) {
    int answer = 0;
    
    dfs("");
    
    auto it = find(words.begin(), words.end(), word);
    int index = it - words.begin();
    
    return index + 1;
}