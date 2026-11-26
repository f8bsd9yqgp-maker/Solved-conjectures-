#include <bits/stdc++.h>
using namespace std;
int main(){
    mt19937 g(192);
    for(int n=4;n<=16;n+=2){
        int count=0, trials=n<=10?10000:n<=12?3000:300;
        for(int t=0;t<trials;t++){
            int a[20][40]={},b[20][20]={};
            for(int i=0;i<n;i++){
                a[i][i+n]=1;
                for(int j=0;j<i;j++) a[i][j]=a[j][i]=b[i][j]=b[j][i]=(g()&1);
            }
            bool ok=true;
            for(int i=0;i<n;i++){
                int j=i;
                while(j<n&&!(a[j][i]&1))j++;
                if(j==n){ok=false;break;}
                for(int k=0;k<2*n;k++)swap(a[i][k],a[j][k]);
                int u=a[i][i];
                for(int k=0;k<2*n;k++)a[i][k]=a[i][k]*u&7;
                for(int j=0;j<n;j++)if(j!=i){
                    int x=a[j][i];
                    for(int k=0;k<2*n;k++)a[j][k]=(a[j][k]-x*a[i][k])&7;
                }
            }
            if(!ok)continue;
            count++;
            int sums[20]={},prev=0,per=0;
            for(int i=1;i<(1<<n);i++){
                int m=i^(i>>1),d=m^prev,j=__builtin_ctz(d),s=m&d?1:-1;
                int p=1;
                for(int k=0;k<n;k++){sums[k]+=s*a[k][j+n];p=p*sums[k]&7;}
                per+=(i&1)?-p:p;
                prev=m;
            }
            if((per&7)!=1){
                cout<<"FOUND "<<n<<" "<<(per&7)<<endl;
                for(int i=0;i<n;i++){
                    for(int j=0;j<n;j++)cout<<b[i][j];
                    cout<<endl;
                }
                return 1;
            }
        }
        cerr<<n<<" "<<count<<endl;
    }
}
