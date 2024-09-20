// Emanuel Wertman
// 9/12
// Calc Lab (short for calculator)
// Extras: Asks user for operator, added  factorial and power operators. (For factorial, it doesn't ask for the 2nd number)

#include <iostream>
#include <cmath>

using namespace std;


bool is_number(const string& s)
{
    string::const_iterator it = s.begin();
    while (it != s.end() && isdigit(*it)) ++it;
    return !s.empty() && it == s.end();
}

int main(){
    string first;
    float newFirst;
    string second;
    float newSecond;
    string oper;
    long long int facto;

    cout << "Welcome to my calc app (short for calculator)" << endl;

    
    cout << "Enter Your First Number: "; 
    getline(cin, first);

    
    cout << "Enter Your Operator (+, -, *, /, %, ++, --, ^, !): "; 
    getline(cin, oper);
    if(oper == "!"){
        facto = stoi(first);
        for(int i = facto-1; i > 1; i--){
            facto *= i;
        }
        cout << facto << endl;
        exit(0);
    }
    else{
        cout << "Enter Your Second Number: "; 
        getline(cin, second);
    }

    if(is_number(first) && is_number(second)){
    newFirst = stoi(first);
    newSecond = stoi(second);
    }
    else{
        cout << "Those aren't numbers!";
        exit(0);
    }


    if(oper == "+"){
        cout << newFirst + newSecond << endl;
    }
    else if(oper == "-"){
        cout << newFirst - newSecond << endl;
    }
    else if(oper == "*" || oper == "x"){
        cout << newFirst * newSecond << endl;
    }
    else if(oper == "/"){
        cout << newFirst / newSecond << endl;
    }
    else if(oper == "^"){
        cout << pow(newFirst, newSecond) << endl;
    }
    else if(oper == "%"){
        cout << static_cast<int>(round(newFirst)) % static_cast<int>(round(newSecond)) << endl;
    }
    else if(oper == "++"){
        newFirst++;
        newSecond++;
        cout << "First: " <<  newFirst << endl;
        cout << "Second: " << newSecond << endl;
    }
    else if(oper == "--"){
        newFirst++;
        newSecond++;
        cout << "First: " <<  newFirst-- << endl;
        cout << "Second: " <<  newSecond-- << endl;
    }
    else{
        cout << "That's not a valid operator!" << endl;
        exit(0);
    }
}

