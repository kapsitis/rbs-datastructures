### Programming task Hairdressers

**Memory limit**: 4 MiB  
**Time limit**: 0.2 second  
**Input file**: `hair.in`  
**Output**: `hair.out`

---

#### Description

In a big city (more than one million of inhabitants, though no more than a billion) there is one and only one hair studio, with only a few hairdressers (their number is up to $9$). Each of the hairdressers has a unique number in $[1..9]$, enabling a more efficient service. The studio measures the time in certain time units $[1\,..\,2\,000\,000\,000]$, and time counting starts at the studio opening moment.

Even though the number of customers is huge and the demand for hairdressers is very high, every hairdresser should take mandatory breaks. The time of a mandatory break for each hairdresser is when the hundreds digit in the time number coincides with the hairdresser’s number. For example, the hairdresser with number $5$ has to take a break in the time intervals $[500..599]$, $[1500..1599]$, $[2500..2599]$, etc. During a break, hairdresser is forbidden to serve a client. In addition, customer appointment cannot be divided in stages, i.e. customer can only be served by one hairdresser without any breaks. Consequently, a hairdresser cannot start to serve a client, if the service cannot be finished before the break starts.

A customer should be served without delay if there is an unoccupied hairdresser and she/he does not have any limitations regarding this work. Upon finishing work with the current client, a hairdresser should immediately try to start serving the next one. More precisely: a client $C_1$ shows up at the time moment $T_1$ and his appointment needs time (serving duration) $D_1$. The hairdresser $H_1$ is currently free. Consequently, this appointment will take place during time interval $[T_1..T_1+D_1-1]$. The appointment is finished at the time moment $T_1+ D_1-1$. If a customer $C_2$ has already shown up before or exactly during time moment $T_1+D_1$, then hairdresser $H_1$ can start working with customer $C_2$ at the time moment $T_1+ D_1$.

Customers wait in a queue, they are admitted on the first come first served basis. At any time moment, no more than one customer can show up. Administrator immediately assigns a number in queue $[1\,..\,200\,000]$ and an appointment duration $[1..900]$.

If there is an unserved customer and there are multiple hairdressers that lay claim on her, then:

1. The hairdresser that has spent more time without a customer (counting from the end of the last appointment), has the priority;
2. If two hairdressers have spent the same time without a client, the hairdresser with the smaller number has the priority.

Knowing the times, when customers show up, their numbers in the queue, the durations of the appointments, our task is to print the appointment end time for each customer, as well as the number of serving hairdresser and the customer's number in the queue. The records should be in ascending order by the appointment finishing time. If two client appointments were finished at the same time, results should be ordered by the hairdresser number.

#### Input: 

The first line has the integer number that is the number of hairdressers. Then follows the information about the customers in the order of showing up (Ascending time values).

```c
Hairdressers
Time Customer Duration
...
0
```

* `Hairdressers` denotes the number of hairdressers $[1..9]$
* `Time` denotes the moment in time, when customer has shown up and is ready to have an appointment $[1\,..\,2\,000\,000\,000]$
* `Customer` denotes the customer number in the queue $[1\,..\,200\,000]$
* `Duration` denotes the necessary length of the appointment $[1..900]$
* `0` means the end of input data. In this case, `Customer` and `Duration` fields are not provided

Input data is in ascending chronological order by `Time`.

The input file is correct regarding the input data format and the given conditions.

#### Output:

According to the input file, each of the customer appointment end time is written in the following format:

```c
Time Hairdresser Customer
```

* `Time` denotes the moment in time, which is the last customer appointment moment $[1\,..\,2\,000\,000\,000]$.
* `Hairdresser` denotes the hairdresser that served the customer, i.e. the hairdresser number $[1..9]$.
* `Customer` denotes the customer that had the appointment - his/her number in queue $[1\,..\,200\,000]$.

In the result, none of the appointment end time will not be greater than $2\,000\,000\,000$.

#### Example:

The content of input file `hair.in`:

```c
2
11 1 10
21 2 50
31 3 20
0
```

The content of output file `hair.out`:

```c
20 1 1
50 1 3
70 2 2
```
