#include <bits/stdc++.h> 

using namespace std; 

int main() { 
    int n; 
    
    while (cin >> n) { 
        int num = 1 % n; 
        int tamanho = 1; 
        
        while (num != 0) { 
            num = ((n + num) * 10 + 1) % n; 
            tamanho++; 
        } 
        
        cout << tamanho << "\n"; 
    } 
    
    return 0; 
}
