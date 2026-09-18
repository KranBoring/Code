#include <bits/stdc++.h>
using namespace std;

bool prime(int n)
{
    if (n<2) return false;
    for (int i = 2; i*i<=n; i++)
        if (n % i == 0) return false;
    return true;
}

int main()
{
    int t;
    if (!(cin >> t)) return 0;
    while (t--)
    {
        int n;
        cin >> n;
        if (prime(n+1)) 
            cout << "YES\n";
        else 
            cout << "NO\n";
    }
    return 0;
}