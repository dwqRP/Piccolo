#include<bits/stdc++.h>
using namespace std;
const int mod=19;

int S[16]={0xe,0x4,0xb,0x2,0x3,0x8,0x0,0x9,0x1,0xa,0x7,0xf,0x6,0xc,0x5,0xd};

int mul(int a,int b){
    int ans=0;
    for(int i=0;i<4;i++){
        if(a&(1<<i)){
            ans^=(b<<i);
        }
    }
    for(int i=7;i>3;i--){
        if(ans&(1<<i)){
            ans^=(mod<<(i-4));
        }
    }
    return ans;
}

int F(int in){
    int tmp[4],res[4],out=0;
    for(int i=0;i<4;i++){
        tmp[i]=in%16;
        in>>=4;
    }
    swap(tmp[0],tmp[3]);
    swap(tmp[1],tmp[2]);
    for(int i=0;i<4;i++)tmp[i]=S[tmp[i]];
    res[0]=mul(2,tmp[0])^mul(3,tmp[1])^tmp[2]^tmp[3];
    res[1]=mul(2,tmp[1])^mul(3,tmp[2])^tmp[0]^tmp[3];
    res[2]=mul(2,tmp[2])^mul(3,tmp[3])^tmp[0]^tmp[1];
    res[3]=mul(2,tmp[3])^mul(3,tmp[0])^tmp[1]^tmp[2];
    for(int i=0;i<4;i++){
        res[i]=S[res[i]];
        out<<=4;
        out|=res[i];
    }
    return out;
}

int main(){
    int din,dout,ans=0;
    cin>>din>>dout;
    int mx=(1<<16);
    for(int i=0;i<mx;i++){
        int delta=F(i)^F(i^din);
        if(delta==dout)ans++;
    }
    printf("%d/%d=%f\n",ans,mx,1.0*ans/mx);
    return 0;
}