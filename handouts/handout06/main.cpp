#include <iostream>
#include <string>

using namespace std;
class Vaccination {
    public:
    string type {}; 
    int year {}; 
};

class Employee {
    public:
    Vaccination v; 
    int energyPoints; 
    virtual void energize() {
        energyPoints += 100;
    }
};

class Manager: public Employee {
    public:
    Manager(Vaccination v, int energyPoints) {
        this -> v = v;
        this -> energyPoints = energyPoints;
    }
    void energize() {
        energyPoints += 123;
    };
};

void energizeTwice(Employee* e) {
    e -> energize();
    e -> energize();
}

int main() {
    Manager m1 { {"Comirnaty", 2021}, 150};
    Manager m2 = m1; 
    m1.energize();
    energizeTwice(&m2);
    return 0;
}
