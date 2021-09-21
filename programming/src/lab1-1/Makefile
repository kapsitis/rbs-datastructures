CPPFLAGS = 
SRC_DIR := .
OBJ_DIR := .

all: sample1.o sample2.o sample3.o sample4.o sample5.o
	g++ -o sample1.out sample1.o
	g++ -o sample2.out sample2.o
	g++ -o sample3.out sample3.o
	g++ -o sample4.out sample4.o
	g++ -o sample5.out sample5.o

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp
	g++ $(CPPFLAGS) -c -o $@ $<

clean:
	rm -f *.out
	rm -f *.o
	rm -f *.out.txt
	
