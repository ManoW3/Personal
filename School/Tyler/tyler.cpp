#include <iostream>
using namespace std;

int main(){

    int age; 
    cout << "How old are you? "; 
    cin >> age; 

    if(age < 8){
        cout << "You are a child";
    }

    else if(age >=8 && age <= 12){
        cout << "You are a tween";
    }
    else if(age >=13 && age <= 18){
        cout << "You are a teen";
    }
    else{
        cout << "You are an adult";
    }
}