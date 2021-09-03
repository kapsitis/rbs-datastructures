#include <iostream> 

using namespace std;
int main() {
  int a, b, c;
  for (int i = 0; i < 3; i++) {
    cin >> a >> b >> c; 
	cin.ignore(1024,'\n');
  }

  cout << a << " " << b << " " << c << endl;
}