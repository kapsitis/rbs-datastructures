### Programming Lab: Airports

**RAM Memory**: 10 MB  
**Time**: 10 second  
**Input**: `lidostas.in`  
**Output**: `lidostas.out`

---

#### Description

To attract new passengers, the national airline organized a lottery. The lottery prize offered to 
travel from any airport to any other - with transfers, if the passenger wants them.
Additionally, the winner also gets 1000 euros. To set limits to the travel, the winner could use a certain flight 
no more than once, and every minute he spends in the airport costs him 1 euro. Once 
a winner runs out of the 1000 euro bonus, he pays for staying in the airports himself.

A single flight is a connection from one airport to another one at a specified hour and minute. 
At another time the flight between the same endpoints is considered another flight.
The same flights repeat day after day.

To transfer between two flights, a passenger needs to spend at least
1 minute in an airport. Namely, if a passenger arrives at `12:34`, then 
at `12:35` s/he can depart with another flight. All clock times are written in format `HH:MM`, where
`HH` means hours `00..23` (prepended with a zero, if necessary), 
and `MM` denotes minutes `00..59` (also prepended with a zero, if necessary). 

For any given airport at every minute there is no more than one departing flight; 
no two flights can leave at the same time. 

The shortest duration of a flight is 30 minutes; the longest duration is 23 hours and 59 minutes. If 
the arrival time is less than the departure time, the arrival happens on the next day. All times are 
written in the same timezone - [Greenwich Mean Time](https://en.wikipedia.org/wiki/Greenwich_Mean_Time). 

A girl named Fortune won the lottery. She wanted to reach her 
destination saving the bonus money (and also her own money).
As she did not know, how to find the optimal itinerary, Fortune chose the following strategy: 
Upon arriving in any airport, she
would take the earliest possible outbound flight (and upon reaching her destination 
she would stop flying).
In this way she expected to pay less money for waiting in the airports. 

The task is to determine, if Fortune can reach her destination by travelling in this manner. 
Your solution should either output the full itinerary (route with all the flights) or a message that it is impossible.

The initial airport has at least one outbound flight, it is known that 
Fortune can leave this airport. 
It is known that all $n$ airports have unique numbers from $1$ to $n$. 
The overall number of flights does not exceed $20\,000$. 



#### Input: 

The 1st line of the input file contains the number of airports. 
The 2nd line contains the origin and the destination airports. The 3rd line 
contains the arrival time in the origin airport. 
(It is possible to leave starting from the arrival time plus 1 minute). 
After that there are lines describing  the flights. 

```c
Airports
Start End
Time
From To n Flight_1 ... Flight_n
...
0
```

* `Airports` - the number of airports (does not exceed $20\,000$); every airport has a unique number between $1$ and this number.
* `Start` - the number of the airport where the itinerary starts.
* `End` - the number of the airport which is the planned destination.
* `Time` - arrival in the start airport, written in format `HH:MM`.
* `From` - the number of the departure airport for the given flight.
* `To` - the number of the arrival airport for the given flight. 
* `n` - the number of flights that will be listed on this line. 
* `Flight_i` - the departure and arrival times in the format `HH:MM-HH:MM`
* `0` - the input file is always terminated with a line containing a single number 0

The lines with flights can have any order.  
Flights between the same two airports may be received on one or several input lines.  
The same flight is never listed twice.

Assume that the input data is correct, it always 
uses the provided format and satisfies the limitations in the problem description.


#### Output:

If it is possible to reach the destination, the output file should have
the starting airport and the arrival time in this airport. After that list the full itinerary 
displaying one flight per line. 

```c
Start Time
From->To Flight
...
```

* `Start` - the airport number where the travel starts.
* `Time` - time when the traveler arrives in the start airport, format is `HH:MM` (same as 3rd line of the input).
* `From` - the departure airport for the current flight.
* `To` - the destination airport for the current flight.
* `Flight` - the departure and arrival times for the flight in the format `HH:MM-HH:MM`.

If it is not possible to do the travel, produce the following output file: 

```c
Impossible
```

#### Example 1 (it is possible to reach the destination):

The contents of the input file `lidostas.in`:

```c
5
1 5
00:00
1 2 1 01:00-03:00
1 2 2 12:00-14:05 15:00-17:00
1 3 2 06:30-08:00 17:20-18:55
2 3 2 13:00-16:00 21:00-00:00
2 4 3 04:00-08:00 05:00-09:00 18:00-22:00
3 1 2 02:45-04:15 23:50-01:20
3 2 1 23:52-02:52
3 5 1 23:51-04:00
4 2 1 18:00-22:00
4 3 1 12:00-13:00
0
```

The content of the output file `lidostas.out`:

```c
1 00:00
1->2 01:00-03:00
2->4 04:00-08:00
4->3 12:00-13:00
3->1 23:50-01:20
1->3 06:30-08:00
3->5 23:51-04:00
```

#### Example 2 (after going from 1 to 2 and back, gets stuck in airport 1):

The content of the input file `lidostas.in`:

```c
3
1 3
00:00
1 2 1 01:00-02:00
2 1 1 03:00-04:00
2 3 1 12:00-13:00
3 2 1 18:00-19:00
0
```

The content of the output file `lidostas.out`:

```c
Impossible
```

