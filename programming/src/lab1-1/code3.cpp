#include <iostream>
#include <string>
#include <vector>

using namespace std;
class Human { 
    protected: 
    string name;
    int energyPoints; 
    public:    
    Human(string name, int energyPoints) {
        this->name = name;
        this->energyPoints = energyPoints;
        cout << "Creating H(" << name << ")" << endl;
    }
    ~Human() {
        cout << "Freeing H(" << name << ")" << endl;
    }
    Human(const Human& h) {
        name = h.name;
        energyPoints = h.energyPoints;
        cout << "Copying H(" << name << ")" << endl;
    }
    virtual string toString() {
        return "H " + name +  " " +  to_string(energyPoints);
    }
    virtual void adjustEnergy() {
        energyPoints += 10;
    }
};

class Manager: public Human {
    public:
    Manager(string name, int energyPoints) : Human(name, energyPoints) {
        cout << "Creating M(" << name << ")" << endl;
    }
    ~Manager() {
        cout << "Freeing M(" << name << ")" << endl;
    }
    virtual void adjustEnergy() {
        cout << " ***********************" << endl;
        energyPoints *= 2;
    }
}; 

int main() {
    int n; 
    cin >> n;
    Human arr[10];


    // vector<Human> humans;
    // for (int i = 0; i < n; i++) {
    //     char type; 
    //     string name;
    //     int energy;
    //     cin >> type >> name >> energy;
    //     if (type == 'H') {
    //         humans.push_back(Human(name, energy));            
    //     }
    //     else {
    //         humans.push_back(Manager(name, energy));
    //     }        
    // }
    // for (vector<Human>::iterator it = humans.begin(); it != humans.end(); ++it) {
    //     (*it).adjustEnergy();
    //     cout << (*it).toString() << endl;
    // }
}

