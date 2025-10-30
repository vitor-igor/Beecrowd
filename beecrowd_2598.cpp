#include <bits/stdc++.h> 

using namespace std; 

int main() { 
    int c; cin >> c;

    int n, m;
    
    while (c--) { 
        cin >> n >> m;

        cout << ceil((double)n / m) << "\n";
    } 
    
    return 0; 
}
