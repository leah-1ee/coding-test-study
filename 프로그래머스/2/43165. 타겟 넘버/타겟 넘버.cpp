#include <string>
#include <vector>

using namespace std;

int count = 0;

void dfs(
    const vector<int>& numbers, 
    int target, 
    int num,
    int i){
    
    if(i==numbers.size()){
        if(num == target) count++;
        return;
    }
    
    dfs(numbers, target, num+numbers[i], i+1);
    dfs(numbers, target, num-numbers[i], i+1);
}

int solution(vector<int> numbers, int target) {
    dfs(numbers, target, 0, 0);
    
    return count;
}