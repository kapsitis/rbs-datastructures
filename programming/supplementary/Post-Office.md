### Programming task Post-Office

**Memory limit**: 20 MB  
**Time limit**: 0.2 second  
**Input file**: `post.in`  
**Output**: `post.out`

---

#### Description

Just before Easter in all post offices of some city the whole unified post office network suddenly stopped working. After having studied the situation, IT specialists let the officers know that this accident was due to a virus (computer virus, not coronavirus SARS-CoV-2), and they cannot get the network up anytime soon. The post-offices slowly started to be overflown by greeting cards, which were not sorted by an automated card sorter, as the computer system ran it.

Head of the office has organized the meeting with her most knowing specialists in order to overcome the current situation. The meeting was also attended by employee Mr. Wiseman, who has been working in the post-office for about half a century. Mr. Wiseman has remembered that in the earlier days card sorting was performed manually and suggested the following option: "*It is most important to sort the cards by their intended destinations. In order to make that easier, the cards should be initially sorted by the first letter of their destination. After that, it is much easier to sort each of the heaps by the destination itself. After that...*". Mr. Wiseman spent the next half an hour talking about how to organize the sorting.

During the first stage, employees acted in the following way:

1.	Each alphabet letter is assigned to one post-office employee. Capital and small letters are treated as the same letter.
2.	Cards are delivered to the employees by a conveyor belt.
3.	Each employee takes the cards assigned to him (i.e. the cards with destination, where the name starts with the alphabet letter assigned to him).
4.	The employee puts the collected letters into one heap.
5.	After that, when there're no more cards on the conveyor belt, the employees take their letters one-by-one from their heap (starting from the top) and put them on the conveyor belt, in order to send them to the next sorting stage
6.	The employees put their cards on the belt in alphabetical order, i.e. the employee assigned the "a" letter is the first one to put his cards on the belt, followed by the employees assigned letters "b", "c", and so forth.

Your task is to make a program that outputs results of the first stage (all 6 steps described above).

#### Input: 

The input file contains destination names separated by one or more spaces.

```c
Name_1 Name_2 ... Name_n
```

* `Name_i` defines the name of the destination. Allowed symbols are only lower case or upper case Latin letters [a..z, A..Z]. Destination name length is within $[1..255]$. 

The maximal size of the file is 1MiB. Destination names may repeat.

The input file is correct regarding the input data format and given conditions.

#### Output:

According to the input file, the output file should contain all destination names separated by single spaces in the following format:

```c
Name_1 Name_2 ... Name_n
```

* `Name_i` defines the name of the destination, where the format is the same as the input file.

If the input file does not contain any destinations, the program should print the word "**nothing**".


#### Example:

The content of input file `post.in`:

```c
suunuciems riiga ventspils daugavpils valmiera valka riiga vecteetinjam saldus valka roja riiga
```

The content of output file `post.out`:

```c
daugavpils riiga roja riiga riiga saldus suunuciems valka vecteetinjam valka valmiera ventspils
```
