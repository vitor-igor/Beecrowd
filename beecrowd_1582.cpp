#include <bits/stdc++.h> 

using namespace std; 

int main() { 
    ios::sync_with_stdio(0);
    cin.tie(nullptr);

    int a, b, c;
    
    while (cin >> a >> b >> c) { 
        if((a * a) == ((b * b) + (c * c)) || ((b * b) == (a * a) + (c * c)) || ((c * c) == (a * a) + (b * b))) {
            if(gcd(gcd(a, b), c) == 1) cout << "tripla pitagorica primitiva\n";
            else cout << "tripla pitagorica\n";
        }
        else cout << "tripla\n";
    } 
    
    return 0; 
}
