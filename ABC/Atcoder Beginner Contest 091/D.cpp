#define ALL(a) (a).begin(),(a).end()
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
        A.push_back(a);
    }
    for (int i = 0; i < N; i++){
        int b;
        cin >> b;
        B.push_back(b);
    }
    vector<vector<int>> BB(30);
    for (int i = 0; i < 30; i++){
        for (int j = 0; j < N; j++){
            BB[i].push_back(B[j] % (1 << i));
        }
    }
    for (int i = 0; i < N; i++){
        int one_count = 0;
        for (int j = 0; j < N; j++){
            one_count += *lower_bound(ALL(BB[i]),(1 << i)-A[i]) + *upper_bound(ALL(BB[i]),(1 << (i+1))-A[i]);
            one_count += *lower_bound(ALL(BB[i]),3*(1 << i)-A[i]) + *upper_bound(ALL(BB[i]),(1 << (i+2))-A[i]);
        }
        if (one_count%2 == 1){
            ans += 1 << i;
        }
    cout << ans << "\n";
    }
    system("PAUSE");
}
// 1 + 2cos^2x = 2 + cos2x 