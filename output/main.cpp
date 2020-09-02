#include<bits/stdc++.h>
#include<bits/stdc++.h>
using namespace::std;
#include<bits/stdc++.h>
using namespace::std;
void B(){
    cout<<"B is included."<<endl;
}

#include<bits/stdc++.h>
using namespace::std;
void C(){
    cout<<"C is included."<<endl;
}


void A(){
    cout<<"A is included."<<endl;
    B();
    C();
}

int main(){
    A();
}
