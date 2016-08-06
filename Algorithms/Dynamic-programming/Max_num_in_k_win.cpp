#include <iostream>
using namespace std;
int main(){
	int n,w;
	cin>>n>>w;
	int a[n+1];
	int k = n-w+1;
	int lr[n+1];
	int rl[n+1];
	int max_val[k+1];
	for(int i=1;i<=n;i++) cin>>a[i];
	for(int i=1;i<=n;i++){
		if(i%w==1) lr[i] = a[i];
		else lr[i] = max(lr[i-1],a[i]);
	}
	for(int i=n;i>0;i--){
		if(i==n) rl[i] = a[i];
		else if(i%w==0) rl[i] = a[i];
		else rl[i] = max(rl[i+1],a[i]);
	}
	for(int i=1;i<=k;i++) {
	max_val[i] = max(rl[i],lr[w+i-1]);
	cout<<max_val[i]<<" ";
	}
	cout<<endl;
	return 0;
}
