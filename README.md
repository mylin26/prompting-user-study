# prompting-user-study

## Overview
This task will center around the creation of an AIware to create the program (aka schedule) of a conference.

Program creation is the process of taking all the accepted papers to a conference and allocating a presentation slot for each paper with parallel sessions. The PC chairs of a conference typically do this manually. Sample programs from the MSR conference can be seen below. Some of the constraints that make the creation of a program challenging are as follows:

### Constraints
- Total time for all presentations in a session cannot be longer than the length of the session.
- Total number of sessions has to be equal to the number of sessions provided by the PC chairs.
- If there are parallel tracks, then no two papers with common authors can be scheduled in parallel at the same time.

When these constraints are met, the PC chairs optimize for the papers in a session to be on a similar topic and work to avoid the parallel scheduling of sessions with related topics. 

### Specification
The input data sources for the challenge comprise of the: 
- Number of conference sessions
- Length of each session (in minutes)
- Number of parallel tracks
- The accepted papers in a particular conference along with all the corresponding data: title, topics, abstract, authors and allocated time for the presentation of each paper

Your software should output the conference program in the JSON object format detailed below.

## Data
The data can be found in the `data` folder. For this task, we are using program data from two conferences: Mining Software Repositories 2022 ([program website](https://conf.researchr.org/program/msr-2022/program-msr-2022/)) and 2023 ([program website](https://conf.researchr.org/program/msr-2023/program-msr-2023/)). You can find the data under `data/msr-2022.json` and `data/msr-2023.json` respectively.

Each talk in the conference is organized in the following JSON format:

```json
{
    "title": "(string) The title of the talk",
    "topics": "(string) The corresponding track (e.g., Data and Tool Showcase Track) or type of paper (e.g., Mining Challenge, Technical Paper)",
    "abstract": "(string) The abstract of the paper",
    "authors": "(object[]) The list of authors in the following JSON format: { \"name\": string, \"institution\": string, \"country\": string }",
    "allocatedTime": "Not available in the data; this will be decided by your AI-powered software.",
    "location": "Not available in the data; this will be decided by your AI-powered software."
}
```
