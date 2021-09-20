CC = g++
CFLAGS =
CPPFLAGS = 

all: sample1 sample2 sample3 sample4 sample5




#sample1: sample1.o
#	g++ -o sample1 sample1.o

#sample% : sample%.o
#	g++ -o $< 

#sample1.o: sample1.cpp
#	g++ -c sample1.cpp

%.o : %.cpp
	$(CC) -c $(CFLAGS) $(CPPFLAGS) $< -o $@

