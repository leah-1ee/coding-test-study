#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    
    int total = brown + yellow;
    
    int width = 3;
    int height;
    for(width; width < brown/2; width++){
        if(total%width != 0) continue;
        height = total / width;
        if(width < height) continue;
        
        if((width-2) * (height-2) == yellow) {
            answer = {width, height};
            break;
        }
    }
    
    return answer;
}