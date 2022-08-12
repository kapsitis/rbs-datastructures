#include <iostream>
#include <queue>

using namespace std;
int main() {
    int n;
    cin >> n; 
    // priority queue (by default it is maximum queue)
    priority_queue<int> queue; 
    // use the standard input to populate the priority queue
    for (int i = 0; i < n; i++) {
        int a; 
        cin >> a;
        queue.push(a); 
    }
    // remove everything until the middle element
    for (int i = 0; i < (n-1)/2; i++) {
        cout << "Ignoring " << queue.top() << endl;
        queue.pop();
    }
    // convert the middle element into a real number
    double result = 1.0*queue.top();
    // if n is even, find average with the other middle element
    if (n % 2 == 0) {
        queue.pop();
        result = (result + queue.top())/2;
    } 
    cout << result << endl;
}