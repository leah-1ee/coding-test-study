#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    
    int best_width = 0;
    int best_height = 0;
    
    for (int i=0; i<sizes.size(); i++){
        int w = max(sizes[i][0], sizes[i][1]);
        int h = min(sizes[i][0], sizes[i][1]);
        
        best_width = max(best_width, w);
        best_height = max(best_height, h);
        
    }
    
    return best_width * best_height;
}