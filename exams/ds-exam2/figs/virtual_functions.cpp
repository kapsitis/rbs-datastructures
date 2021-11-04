class Node {
public:
    string label;
    virtual string toString() = 0;
};

class Leaf : public Node {
public:
    Leaf(string arg) { label = arg; }
    virtual string toString()
    {
      // TODO: Insert your code here
    }
};

class Internal : public Node {
public:
    list<Node *> children;
    Internal(string arg, list<Node *> ch)
    {
        label = arg;
        children = ch;
    }
    virtual string toString()
    {
      // TODO: Insert your code here
    }
};

int main() {
    Node *tree1Root = new Leaf("AAA");
    cout << tree1Root->toString() << endl << endl;
	
    Node *tree2Root = new Internal("AA", 
        {new Leaf("BB"), new Leaf("CC")});
    cout << tree2Root->toString() << endl << endl;
	
    Node *tree3Root = new Internal("A",
        {new Internal("B", {
            new Internal("C", {new Leaf("D"), new Leaf("E")}),
            new Internal("F", {new Leaf("G"),
                new Internal("H", {new Leaf("I"), new Leaf("J")})}),
        }),
        new Internal("K", {new Internal("L", {new Leaf("M")})})});
    cout << tree3Root->toString() << endl
         << endl;
}