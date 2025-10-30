#include <bits/stdc++.h>

using namespace std;

int main() {
    int n; cin >> n;

    while(n--) {
        int f1, f2; cin >> f1 >> f2;

        cout << gcd(f1, f2) << "\n";
    }

    return 0;
}