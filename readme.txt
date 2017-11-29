
YOUR TASK:
----------

Take a look at the code in this codebase. In what ways can it be improved?
Consider the following aspects specifically:
  - Readability
  - Reusability
  - Modularity
  - Scalability
  - Runtime performance
  - Conformance to standards and best practices

Your task is to edit this code to enforce as much of the previous improvements as possible. Don't worry if you don't understand enough about the code to suggest specific improvements. Do you best and make reasonable assumptions and educated guesses.

When not sure, you can still suggest non-specific edits. For example, if you don't know what a function is doing but still think it needs a descriptive comment, insert one that says: "descriptive comment here to explain x,y,z"


IMPORTANT INSTRUCTIONS:
-----------------------

1- Go ahead and fork this repo. In your forked repo, create a branch off master, naming it: yourfirstname_yourlastname
2- You may do multiple commits to your branch, incrementally refactoring the code as needed
3- When finished, push your commits to github, following best practicies as you would in a production setting
4- Please do not merge your edits back to master
5- When done, please send us a link to your repo, making sure we have read permissions to it.

INIT
----
pip install pyexcel
pip install matploblib
pip install pandas
pip install sklearn
pip install scipy
pip install dill

Overall Design of Cognoa DS lib
----
It looks like there are two versions of the dataset that we can currently operate on: V1, V2
Each of the datasets is a set of questions in which parents fill out a form and answer, and we
are trying to reason about these answers and us ML to determine disorders and risks.

I would reorganize by splitting the folder into generic helper functions such as the plotting tools
and cognoa specific functionality.

Overall I would create classes for each version of the question set. Each class would contain its
own calculator, and have adaptors to convert to other versions. This would allow for much more readability
and for new versions to be easily introduced.

More Todos
----
- it looks like `ados1_b4` values should go into an enum and each value should be documented and have a meaning
- In cog_calculators:
  - risk levels should be an enum
- In video_analyst_lib:
  - this file should be split up into multiple files
