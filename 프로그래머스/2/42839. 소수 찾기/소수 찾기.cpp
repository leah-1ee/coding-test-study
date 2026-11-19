#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

bool isPrime(int num){
    if (num < 2) return false;
    for(int i=2; i * i <= num; i++){
        if(num%i == 0) return false;
    }
    return true;
}

int solution(string numbers) {
    sort(numbers.begin(), numbers.end());
    
    set<int> primes;
    
    do{
        for(int len=1; len<=numbers.size(); len++){
            int n = stoi(numbers.substr(0, len));
            if(isPrime(n)) primes.insert(n);
        }
    } while(next_permutation(numbers.begin(), numbers.end()));
    
    return primes.size();
}