#include <iostream>
using namespace std;

int a;
char letter;
char temp;
float b;
bool run;
string sigma;
int main(){
    a = 10;
    letter = 'a';
    b = 10.0;
    cout << "Do you want a to say Hello Sigma? (y/n) " << endl;
    cin >> temp;
    if (temp == 'y') {
        run = true;
    }

    else {
        run = false;
    }
    sigma = "Hello Sigma";
        if (a == b && run) {
            cout << letter << " says " << sigma << endl;
        }
        else {
            cout << letter << " doesn't say " << sigma << endl;
        }

}