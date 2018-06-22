#include<vector>
#include<iostream>
#include<string>

using namespace std;

class stack
{vector <char> vec;
 vector <char> :: iterator itr;
 public:
 void push(char);
 char pop();
 int isempty();
};

void stack :: push(char val)
{vec.push_back(val);
}

char stack :: pop()
{itr=--vec.end();
char n=*itr;
vec.erase(itr);
return n;
}

int stack :: isempty()
{if(vec.empty())
return 0;
else
return 1;
}

int main()
{stack s;
 char c[100],b[100];
 int n;
 cout<<"enter the string to be reversed"<<endl;
 cin.get(c,100);
 for (int i=0;c[i]!='\0';i++)
 { s.push(c[i]);
 }
 for (int i=0;c[i]!='\0';i++)
 {	n=s.isempty();
	if (n==1)
 	b[i]=s.pop();
 }
 cout<<b;
 return 0;
}
