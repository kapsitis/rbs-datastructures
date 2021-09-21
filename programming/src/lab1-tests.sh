#!/bin/bash
#must have sudo rights

#echo "Pulling from git..."
#echo "-----------------------------"
#git clone git@github.com:jekabssolo/workspace-cpp.git
#cd workspace-cpp
#git checkout ex03-alice
cd lab1-1

echo "***** sample1.cpp *****"
echo "Compiling..."
echo "-----------------------------"
g++ -c sample1.cpp -o sample1.out
chmod u+x sample1.out

echo "----- input1-01.txt -----"
./sample1.out < input1-01.txt > output1-01.txt
diff -i -B output1-01.txt expected1-01.txt
echo "-----------------------------"
echo "Compiled!"
exit 0

echo
echo
echo
echo "Starting tests..."
echo
echo
echo "-----------------------------"
echo "Starting test No. 1"
time ./ex03alice < tests/test01in.txt > tests/test01out.txt
echo
diff -s -B tests/test01out.txt tests/test01expected.txt
echo "-----------------------------"
echo
echo "-----------------------------"
echo "Starting test No. 2"
time ./ex03alice < tests/test02in.txt > tests/test02out.txt
echo
diff -s -B tests/test02out.txt tests/test02expected.txt
echo "-----------------------------"
echo
echo "-----------------------------"
echo "Starting test No. 3"
time ./ex03alice < tests/test003in.txt > tests/test03out.txt
echo
diff -s -B tests/test03out.txt tests/test03expected.txt
echo "-----------------------------"
echo
echo "-----------------------------"
echo "Starting test No. 4"
time ./ex03alice < tests/test04in.txt > tests/test04out.txt
echo
diff -s -B tests/test04out.txt tests/test04expected.txt
echo "-----------------------------"
echo
echo "Cleaning up..."
rm ./ex03alice & rm ./Node.o & rm ./AliceMain.o
rm ./tests/test01out.txt ./tests/test02out.txt ./tests/test03out.txt ./tests/test04out.txt
cd ../../
sudo rm -r workspace-cpp
echo
echo "Done!"
