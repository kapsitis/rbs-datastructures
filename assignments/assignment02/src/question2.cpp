#include <iostream>

struct Node { int info; Node * next; };

using namespace std;
void checkAndDeleteThirdNode(Node * & arg) {
    arg = arg -> next -> next;
    if (arg -> next -> info == 17) { 
        arg -> next = arg -> next -> next; 
    }
}

void insert(Node*& first, Node*& last, int a) {
    Node* node = new Node; 
    node -> info = a; 
    node -> next = NULL;
    if (first == NULL) {
        first = node;
        last = node;
    }
    else {
        last -> next = node;
    }
    last = node;
}

void printAll(Node* current) {
    cout << "["; 
    while (current != NULL) {
        cout << current -> info;        
        current = current -> next;
        if (current != NULL) {
            cout << " "; 
        }
    }
    cout << "]" << endl;
}

int main() {
    int n; 
    cin >> n;
    Node* first = NULL;
    Node* last = NULL;
    for (int i = 0; i < n; i++) {
        int a; 
        cin >> a;
        insert(first,last,a);        
    }
    checkAndDeleteThirdNode(first);
    printAll(first);
}
