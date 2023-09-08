#include <bits/stdc++.h>
#include <atcoder/all>
#define ll long long
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using namespace atcoder;
using mint = modint;
int mod = 998244353;
long long modpow(long long a, long long n, long long mod) {
    long long res = 1;
    while (n > 0) {
        if (n & 1) res = res * a % mod;
        a = a * a % mod;
        n >>= 1;
    }
    return res;
}
vector<ll> vslice(vector<ll> x,ll l,ll r){
    vector<ll> ans;
    for (ll i = l; i < r; i++){
        ans.emplace_back(x[i]);
    }   
    return ans;
}
class FPS{
    public:
    vector<ll> fps;
    int deg;
    FPS(vector<ll> f){
        fps = f;
        deg = f.size();   
    }
    vector<ll> get_list() {return fps;}
    int get_deg() {return deg;}
    FPS operator*(FPS g){
        FPS c = FPS(convolution(fps,g.fps));
    return c;
    }
    FPS operator*=(FPS g){
        FPS c = FPS(convolution(fps,g.fps));
        fps = c.fps;
        deg = c.deg;
        return *this;
    }
    FPS log(int n){
        if (fps[0] != 1){
            return FPS({0});
        }
        else{
            FPS dif_div_fx = (((*this).differ(n)) * ((*this).inverse(n))).intergal(n);
            return dif_div_fx;
        }
    }
    FPS differ(int n){
        vector<ll> ans;
        rep(i,min(n,deg-1)){
            if (i == 0){
                continue;
            }
            ans.emplace_back((i+1)*fps[i+1]);
        }
        return FPS(ans);
    }
    FPS intergal(int n){
        vector<ll> ans;
        ans.emplace_back(0);
        rep(i,min(n,deg-1)){
            ans.emplace_back(fps[i] * modpow((i+1),mod-2,mod));
        }
        return FPS(ans);
    }
    FPS operator+(FPS g){
        rep(i,max(deg,g.deg)){
            if (g.deg <= i){
                g.fps.emplace_back(0);
                g.deg++;
            }
            else if (deg <= i){
                fps.emplace_back(0);
                deg++;
            }
            else{
                
            }

        }
    }
    FPS exp(int n){
        if (fps[0] != 0){
            return FPS({0});
        }
        else{
            FPS g = FPS({1});
            FPS co = FPS({1});
            FPS f_k = FPS(fps);
            rep(i,n-1){
                co *= FPS({modpow(i+1,mod-2,mod)});

            }
        }
    }
    FPS operator^(int n){

    }
    FPS inverse(int n){
        int h = 1;
        while ((1 << h) < n){
            h++;
        }
        FPS g = FPS({modpow(fps[0],mod-2,mod)});
        rep(i,h){
            FPS gn_f = FPS(vslice(fps,0,2<<(i+1))) * g;
            rep(k,gn_f.fps.size()){
                gn_f.fps[k] = mod-gn_f.fps[k];
            }
            gn_f.fps[0] += 2;
            g = FPS(vslice((g * gn_f).fps,0,2<<(i+1)));
        }
        vector<ll> ans;
        rep(i,n){
            ans.emplace_back(g.fps[i]);
        }
        FPS a = ans;
        return a;
    }
    FPS operator/(FPS g){
        if (g.deg > deg){
            return FPS({0});
        } 
        else{
            vector<ll> tf;
            rep(i,g.deg){
                tf.emplace_back(g.fps[g.deg-i-1]);
            }
            FPS f = tf;
            FPS cf = f.inverse(deg);
            vector<ll> c;
            rep(i,g.deg-f.deg-1){
                c.emplace_back(0);
            }
            c.emplace_back(1);
            FPS fpc = c;
            FPS ans = cf * fpc;
            vector<ll> gf;
            rep(i,deg){
                gf.emplace_back(fps[deg-i-1]);
            }
            FPS result = ans * FPS(gf);
            vector<ll> tmp;
            rep(i,deg - g.deg + 1){
                tmp.emplace_back(result.fps[i]);
            }
            reverse(tmp.begin(),tmp.end());
            return FPS(tmp);
        }
    }
};
int main(){
    ll mindeg;
    ll N,K;
    cin >> N >> K;
    vector<ll> tmp(N+10,0);
    FPS f = tmp;
    rep(i,K){
        ll l, r;
        cin >> l >> r;
        rep(j,r-l+1){
            f.fps[j+l] -= 1;
        }
    }
    f.fps[0] += 1;
    f = f.inverse(N+10);
    cout << f.fps[N-1];
}