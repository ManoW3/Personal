#include <iostream>
using namespace std;

int main()
{
    string streetName;
    cout << "What is your street name: "; 
    getline(cin, streetName);
    
    string name;
    cout << "What is your real name: "; 
    getline(cin, name);
    
    string hood;
    cout << "What is your hood: "; 
    getline(cin, hood);
    
    string passtime;
    cout << "What is your favorite passtime: "; 
    getline(cin, passtime);
    
    string language;
    cout << "What is your favorite coding language: "; 
    getline(cin, language);
    
    string phone;
    cout << "Apple or Samsung? "; 
    getline(cin, phone);
    
    
    
    cout << "One day, " << name << " who goes by " 
    << streetName << " left his home in the poverty-stricken " << hood << " to go " 
    << passtime << " while coding in "<< language << " on his " 
    << phone << " phone" << endl;
    
    return 0;
}