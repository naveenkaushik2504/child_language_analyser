# Child Language Analyser

## Dataset
The dataset is known as ENNI [https://childes.talkbank.org/access/Clinical-MOR/
ENNI.html] which is a collection of narrative transcripts gathered for a clinical study carried out
in Alberta, Canada, to study children with language disorders. Two sets of data were collected:
the first set is from children diagnosed with Specific Language Impairment (SLI) — one form
of language disorders; and the second set is from children with the typical development (TD).
A subset of the original corpus is used in this code with 10 selected transcripts for each
group of children.

Each of the narrative transcripts is a record of the story-telling task performed by a child for
the two groups (SLI and TD), under the supervision of an examiner (investigator).

### Task 1: Handling with File Contents and Preprocessing
In the first task, you will begin by reading in all the transcripts of the given dataset, for both
the SLI and TD groups. We will then conduct a number of pre-processing tasks to extract
only the relevant contents or texts needed for analysis in the subsequent tasks (Task 2 and 3)
in this assignment. Upon completing the pre-processing tasks, each of the cleaned transcript
should be saved as an individual output file.

(a) Remove those words that have either ‘[’ as prefix or ‘]’ as suffix1 but retain these three
symbols: [//], [/], and [*]2
Example:
Before filtering: *CHI: then [/-] the doctor give the [/] money to the man .
After filtering: then the doctor give the [/] money to the man .
(b) Retain those words that have either ‘<’ as prefix or ‘>’ as suffix but these two symbols
should be removed
Example:
Before filtering: *CHI: <he> [/] <he> [/] he hold it .
After filtering: he [/] he [/] he hold it .

(c) Remove those words that have prefixes of ‘&’ and ‘+’
Example:
Before filtering: *CHI: &=sighs <and instead the> [//] and then the giraffe got
it and gave it to the elephant .
After filtering: and instead the [//] and then the giraffe got it and gave it to
the elephant .
(d) Retain those words that have either ‘(’ as prefix or ‘)’ as suffix but these two symbols
should be removed
Example:
Before filtering: *CHI: and then (.) the little (.) giraffe is crying because it (i)s
sinking .
After filtering: and then (.) the little (.) giraffe is crying because it is sinking .

Finally, save the cleaned SLI transcripts under a folder named “SLI_cleaned”, and the
cleaned TD transcripts under another new folder named “TD_cleaned”.

### Task 2: Building a Class for Data Analysis
The statistics for each of child transcript that we are interested in are:
- Length of the transcript — indicated by the number of statements
- Size of the vocabulary — indicated by the number of unique words
- Number of repetition for certain words or phrases — indicated by the CHAT symbol [/]
- Number of retracing for certain words or phrases — indicated by the CHAT symbol [//]
- Number of grammatical errors detected — indicated by the CHAT symbol [*]3
- Number of pauses made — indicated by the CHAT symbol (.)


### Task 3: Building a Class for Data Visualisation
In the last task, you will implement a class to visualise the statistics collected in 
Task 2 as some form of graphs.

## Prerequisites
Python version 3.6.5

## Running
```
python basic_game.py 
python extended_game.py
```

