# Embedded Systems - Real-Time Systems

Embedded Systems - Sharif University of Technology

* Embedded System Instructor: Dr. Mohsen Ansari
* Real Time Instructor: Dr. Sepideh Safari

## Contents
### Fixed Priority Servers
Assumption: Periodics are scheduled under RM (utilization bound = n(2^(1/n)-1) ).

- Polling Server
  - The server asks periodically from aperioci tasks if there are any aperiodic ones.
  
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
  - RT = Replenishment Time = t_A + T_S
  - RA = Replenishment Amount = the capacity consumed at [t_A, t_i].
  - t_i = the last time that SS is active (SS is active when the aperiodic task is running or the task that is running, has a higher priority than aperiodic one).
  - comsuming server capacity is gradually but charging is suddenly (at once, the server capacity is increased by RA).
  - Question: What if the RA continues till RT?!

- Slack Stealing
  - slack_time = abs_deadline - time - remaining_c
  - Policy: Shift everything in a way that periodic tasks dont miss!


### Dynamic Priority Servers
Question: Why do we call it "dynamic"?

Goal: Enhance Average Response Time of Aperiodic Tasks (without compromising schedulability of hard periodic tasks)

Assumption: Periodic tasks are scheduled by EDF (utilization bound = 1).

Assumption: All periodic tasks have hard deadlines, and aperiodics dont have deadline and they should be scheduled ASAP.

- Dynamic Priority Exchange (DPE) Server
  - server can trade its capacity with lower-priority tasks (EDF: has longer deadline).
  - server capacity (runtime is never wasted?!).
- Dynamic Sporadic Server
  - extension of SS
  - Question: Difference between it and fixed one?
 

## TO DO
- Add the scheduling algorithms and their Demo (Visualization)
- Add different algorithms (code) in the real-time systems course
- Upload the lecture notes
- Upload useful slides
- Upload Useful assignments and answers
- Add links of useful courses (videos) and their assignments with answers
- The previous suggestion can be converted into a bank of questions that is useful for teaching assisstants to design homeworks
- Upload the source books of both courses
