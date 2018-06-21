#include<vector>
#include<iostream>

using namespace std;

class stack
{vector <int> vec;
 vector <int> :: iterator itr;
 public:
 void push(int);
 int pop();
 int isempty();
 void display();
}

void stack :: push(int val)
{vec.push_back(val);
}

int stack :: pop()
{int val=vec.rbegin();
int n=*val;
vec.erase(val);
return n;
}

int stack :: isempty()
{if(vec.empty())
return 0;
else
return 1
}


void stack :: display()
{for(itr=vec.begin();itr!=vec.end(); ++itr)
cout<<*itr<<endl;
}

int main()
{stack s;
int n,val;
do
{cout<<"Enter the choice-\n 1-Push an integer\n2-Pop an integer\n3-Display the stack\n4-Exit\n";
cin>>n;
switch(n)
{case 1:
	cout<<"Enter the number to be pushed\n";
	cin>>val;
	if(val>0 && val<25000)
	{s.push(val);
	 cout<<val<<" was successfully pushed into the stack\n";
	}
	break;
case 2:
	val=s.isempty();
	if (val==0)
	cout<<"Stack is empty\n";
	else
	val=s.pop();
	cout<<val<<" was successfully popped out of the stack\n";
	break;
case 3:
	val=s.isempty();
	if (val==0)
	cout<<"Stack is empty\n";
	else
	s.display();
	break;
case 4:
	break;
default: 
	cout<<"Enter valid choice\n";
	break;
}
}while(n!=3)
}
        
	return 0;
}
