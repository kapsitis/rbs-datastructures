#!/bin/bash
#must have sudo rights

#echo "Pulling from git..."
#git clone git@github.com:username/ds-workspace-username.git

declare -a tsts=("01" "02" "03" "04" "05")

cd lab1-1
make clean


echo "-----------------------------"
echo "******** sample1.cpp ********"
echo "-----------------------------"
echo "Compiling..."
make sample1
FILE=sample1
if test -f "$FILE"; then
  for i in "${tsts[@]}"
    do
      echo "----- test1.${i}.txt -----"
      ./sample1 < test1.${i}.txt > test1.${i}.out.txt
      diff -i -w -B test1.${i}.out.txt expected1.${i}.txt | head -4
      echo "------------------------"
    done
grades=()
grades+=("QQ1")
grades+=("QQ2")
grades+=("QQ3")
for value in "${grades[@]}"
  do
    echo $value
  done


echo 

echo "-----------------------------"
echo "******** sample2.cpp ********"
echo "-----------------------------"
echo "Compiling..."
make sample2.out
for i in "${tsts[@]}"
do
   echo "----- test2.${i}.txt -----"
   ./sample2 < test2.${i}.txt > test2.${i}.out.txt
   diff -i -w -B test2.${i}.out.txt expected2.${i}.txt | head -4
   echo "------------------------"
done
echo 


echo "-----------------------------"
echo "******** sample3.cpp ********"
echo "-----------------------------"
echo "Compiling..."
make sample3.out
for i in "${tsts[@]}"
do
   echo "----- test3.${i}.txt -----"
   ./sample3 < test3.${i}.txt > test3.${i}.out.txt
   diff -i -w -B test3.${i}.out.txt expected3.${i}.txt | head -4
   echo "------------------------"
done
echo 


echo "-----------------------------"
echo "******** sample4.cpp ********"
echo "-----------------------------"
echo "Compiling..."
make sample4.out
for i in "${tsts[@]}"
do
   echo "----- test4.${i}.txt -----"
   ./sample4 < test4.${i}.txt > test4.${i}.out.txt
   diff -i -w -B test4.${i}.out.txt expected4.${i}.txt | head -4
   echo "------------------------"
done
echo 



echo "-----------------------------"
echo "******** sample5.cpp ********"
echo "-----------------------------"
echo "Compiling..."
make sample5.out
for i in "${tsts[@]}"
do
   echo "----- test5.${i}.txt -----"
   ./sample5 < test5.${i}.txt > test5.${i}.out.txt
   diff -i -w -B test5.${i}.out.txt expected5.${i}.txt | head -4
   echo "------------------------"
done
echo 


cd ../
cd lab1-2
make clean


echo "-----------------------------"
echo "******** sample6.cpp ********"
echo "-----------------------------"
echo "Compiling..."
make sample6.out
for i in "${tsts[@]}"
do
   echo "----- test6.${i}.txt -----"
   ./sample6 < test6.${i}.txt > test6.${i}.out.txt
   diff -i -w -B test6.${i}.out.txt expected6.${i}.txt | head -4
   echo "------------------------"
done
echo 


echo "Cleaning up..."
#make clean
cd ../
#sudo rm -fr ds-workspace-username/
echo
echo "Done!"
