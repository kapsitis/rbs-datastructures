#include <iostream>
#include <stack>
using namespace std;
class Pair { 
  public: int x; int y; 
  Pair() { 
    cout << "Default constructor" << endl; 
  }
  Pair(const Pair& arg) { 
    cout << "Copy constructor on (" << x << "," << y << ")" << endl; 
    x = arg.x;
    y = arg.y;
  }
  ~Pair() {
    cout << "Destructor on (" << x << "," << y << ")" << endl; 
  }

}; 
istream &operator>>(istream  &input, Pair &p ) { 
  input >> p.x >> p.y;   return input;            
}
ostream &operator<<(ostream &output, const Pair &p ) { 
  output << "(" << p.x << "," << p.y << ")";   return output;            
}
bool operator<(const Pair &left, const Pair &right) {
  return (left.x < right.x) || (left.x == right.x && left.y < right.y);
}
int main() {

    int n; 
    cin >> n; 
    stack<Pair> myStack;
    for (int i = 0; i < n; i++) {
        Pair p; 
        cin >> p;
        if (myStack.empty() || myStack.top() < p) {
            myStack.push(p);
        }        
    }
    stack<Pair> otherStack;
    while (!myStack.empty()) {
        otherStack.push(myStack.top());
        myStack.pop();
    }    

    while (!otherStack.empty()) {
        cout << otherStack.top() << endl;
        otherStack.pop();
    }      
}
