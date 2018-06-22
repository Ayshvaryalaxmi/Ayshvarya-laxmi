#include <iostream>
#include<string>
using namespace std;

int main() {
	char str[100],word[20];
	int i,j=0;
	cout<<"enter the string\n";
	cin.get(str,100);
	for(i=0;str[i]!='\0';i++)
	{if(str[i]!=' ')
	 {word[j]=str[i];
	  j++;
	 }
	 else
	 {word[j]='\0';
	  word[0]=toupper(word[0]);
	  cout<<word<<' ';
	  j=0;
	 }
	}
	word[j]='\0';
	word[0]=toupper(word[0]);
	cout<<word<<' ';
	return 0;
}
