# Embedded Systems - Real-Time Systems

Embedded Systems - Sharif University of Technology

* Embedded System Instructor: Dr. Mohsen Ansari
* Real Time Instructor: Dr. Sepideh Safari

## Contents
### Fixed Priority Servers
- Polling Server
- Deferrable Server
  
  - In this algorithm we have a server, and it has a priority based on its rate (if the algm is RM).
  - In the periods, it is charged up to its capacity (wcet aperiodic).
  - The difference between this algorithm and the "Polling Server" is that polling server polls and asks in a periodic way if there are any aperiodic tasks waiting, but deferrable server waits for the aperiodic task to come.

- Priority Exchange

  - This algorithm is created for soft real-time aperiodic tasks.
  - It has worse performance in terms of DS (Deferrable Server).
  - The server capacity is passed through other tasks so that it can take the capacity back for executing aperiodic tasks.

- Sporadic Server
  - It enhances average response time of aperiodic tasks without degrading the utilization bound for periodic tasks.
  - It shifts the time of charging the server capacity.


  
  
  

### Dynamic Priority Servers


## TO DO
- Add the scheduling algorithms and their Demo (Visualization)
- Add different algorithms (code) in the real-time systems course
- Upload the lecture notes
- Upload useful slides
- Upload Useful assignments and answers
- Add links of useful courses (videos) and their assignments with answers
- The previous suggestion can be converted into a bank of questions that is useful for teaching assisstants to design homeworks
- Upload the source books of both courses
