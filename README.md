# prompting-user-study

## Overview
This task will center around the creation of an AIware to create the program (aka schedule) of a conference.

Program creation is the process of taking all the accepted papers to a conference and allocating a presentation slot for each paper with parallel sessions. The PC chairs of a conference typically do this manually. Sample programs from the MSR conference can be seen below. Some of the constraints that make the creation of a program challenging are as follows:

### Constraints:
- Total time for all presentations in a session cannot be longer than the length of the session.
- Total number of sessions has to be equal to the number of sessions provided by the PC chairs.
- If there are parallel tracks, then no two papers with common authors can be scheduled in parallel at the same time

When these constraints are met, the PC chairs optimize for the papers in a session to be on a similar topic and work to avoid the parallel scheduling of sessions with related topics. The input data sources for the challenge comprise the number of conference sessions, the length of each session, the number of parallel tracks, and the accepted papers in a particular conference along with all the corresponding data: title, topics, abstract, paper, authors and allocated time for the presentation of each paper. 

## Data
The data can be found in the `data` folder.
