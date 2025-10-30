#include <bits/stdc++.h> 

using namespace std; 

bool eh_primo(int n) {
    if(n == 1) return false;
    if(n == 2) return true;
    if(n % 2 == 0) return false;
    
    for(int i = 3; i * i <= n; i++) if(n % i == 0) return false;

    return true;
}

int main() { 
    ios::sync_with_stdio(0);
    cin.tie(nullptr);

    int n; cin >> n;
    
    while (n--) { 
        int num; cin >> num;
        
        if(eh_primo(num)) cout << "Prime" << "\n";
        else cout << "Not Prime" << "\n";
    } 
    
    return 0; 
}
