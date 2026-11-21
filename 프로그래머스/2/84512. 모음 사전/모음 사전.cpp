#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string vowels = "AEIOU";

vector<string> dictionary;

void dfs(string word){
    if(word.size() == 5) return;
    
    for(char c:vowels){
        string next = word + c;
        dictionary.push_back(next);
        dfs(next);
    }

}

int solution(string word) {
    
    dfs("");
    auto it = find(dictionary.begin(), dictionary.end(), word);
    int index = it - dictionary.begin();
    
    return index + 1;
}