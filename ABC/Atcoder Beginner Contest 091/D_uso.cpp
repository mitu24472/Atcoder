#pragma GCC optimize ("Ofast")
#pragma GCC target ("avx512f")
#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    cin >> N;
    vector<int> A, B;
    int ans = 0;
    for (int i = 0; i < N; i++){
        int a;
        cin >> a;
        A.emplace_back(a);
    }
    for (int i = 0; i < N; i++){
        int b;
        cin >> b;
        B.emplace_back(b);
    }
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            ans =  (A[i]+B[j]) xor ans;
        }
    }
    cout << ans;
}