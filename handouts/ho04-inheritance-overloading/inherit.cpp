#include <iostream>
#include <string>

using namespace std;
class Rectangle {
    protected:
    int width, height; 
    public:
    string color;
    Rectangle(int width, int height) {
        this->width = width; 
        this->height = height;
        color = "gray";
    }    

    void makeWider() {
        width *= 2; 
    }
};

class Square: public Rectangle {
    public:
    Square(int size): Rectangle(size, size) {
        color = "red";        
    }
    void makeWider() {
        width *= 2;
        height *= 2;
    }
};

int main() {
    Square s1(17);
    Square s2 = s1;
    s1.makeWider();
    Rectangle* r2 = &s2;
    r2 -> makeWider();
}
