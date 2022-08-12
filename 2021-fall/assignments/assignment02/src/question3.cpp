#include <iostream>
#include <string>

using namespace std;
class Human { 
    protected: 
    string name;
    int energyPoints; 
    public:
    Human() {}
    Human(string name, int energyPoints) {
        this->name = name;
        this->energyPoints = energyPoints;
        cout << "Creating H(" << name << ")" << endl;
    }
    virtual ~Human() {
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
    string toString() {
        return "M " + name +  " " +  to_string(energyPoints);
    }
    void adjustEnergy() {
        energyPoints *= 2;
    }
}; 

int main() {
    int n; 
    cin >> n;
    Human** humans = new Human*[n];

    for (int i = 0; i < n; i++) {        
        char type; 
        string name;
        int energy;
        cin >> type >> name >> energy;
        if (type == 'H') {
            humans[i] = new Human(name,energy);
        }
        else {
            humans[i] = new Manager(name,energy);
        }
    }
    for (int i = 0; i < n; i++) {
        humans[i] -> adjustEnergy();
    }
    for (int i = 0; i < n; i++) {
        cout << humans[i] -> toString() << endl;
        delete humans[i];
    }

    delete[] humans;
}

