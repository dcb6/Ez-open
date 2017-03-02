# ez-open
Open all of the necessary files and websites for one task, easily. (Mac only)

## The problem
When I want to start any task, whether its completing a homework assignment or working on a coding project, I have to open several websites, pdfs, etc. spread out across my computer. The time that these transitions take adds up!

## The solution
With ez-open, you can assign groupings of files and websites, and open any number of groupings quickly and easily from the Terminal.

### Example:

I want to work on problems 2 and 3 of my COMP 182 assignment and open up the main problem page. After quickly setting up ezopen, I type

`python ezopen.py 2 3 main`

And this opens up the appropriate Overleaf, assignment webpages, and pdfs for these problems.

## Usage
The first time running ez-open, type

`python ezopen.py setup firsttime`

This will perform the normal setup procedure with extra intruction. Follow the instructions. From then on, whenever you want to open a grouping, type commands in the form

`python ezopen.py keyword1 keyword2 keyword3`

Where each keyword is one of the keywords set by you. Order doesn't matter!

## Improvements
Currently working on several important options such as grouping the keywords and being able to edit the setup.
