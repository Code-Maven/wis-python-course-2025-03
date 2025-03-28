# WIS Python programming course started in 2025.03

Course number: 20253072

* Direct link to [course information](https://erez.weizmann.ac.il/pls/htmldb/f?p=186:30:::NO::pid,pprev:15101,14800)
* Feinberg [Moodle](https://feinberg.weizmann.ac.il/)

* Location: Feinberg Room B

## Students

| Home page | Repo | Assignments | Project | Status |
| --------- | ---- | ----------- | ------- | ------ |


<!--
| []()                | [repo]()                     |  |  |  |
-->


## Lecturer

* [Gábor Szabó](https://szabgab.com/)

## Teaching Assistants

* [Hadar Klimovski](https://hadarklimovski.github.io/)
* [Liron Hoffman](https://liroh99.github.io/)

## Plan

[SYLLABUS](SYLLABUS.md)

### Schedule

* [Day 1](#Day-1) 2025.03.27 9:00-12:00
* [Day 2](#Day-2) 2025.04.03 9:00-12:00
* [Day 3](#Day-3) 2025.04.10 9:00-12:00
* Passover
* [Day 4](#Day-4) 2025.04.24 9:00-12:00
* Independence day
* [Day 5](#Day-5) 2025.05.08 9:00-12:00
* [Day 6](#Day-6) 2025.05.15 9:00-12:00
* [Day 7](#Day-7) 2025.05.22 9:00-12:00
* [Day 8](#Day-8) 2025.05.29 9:00-12:00
* [Day 9](#Day-9) 2025.06.05 9:00-12:00
* [Day 10](#Day-10) 2025.06.12 9:00-12:00


### Assignments

There will be assignments after every lecture. You will submit them via GitHub. I'll explain the details during the lectures.

### Extensions

Each assignment and the project will have dead-lines. If you need to ask for extensions, do it up-front asking your TA.
Make their life easier and ask specify the new dead-line you need.


### Project

Towards the end of the course you'll be asked to do a project.
First you will need to submit a proposal for the project and when it is accepted then implement it.
The project should be something that is useful for your studies or at least it is fun for you to make.
Ask in the lab where you work what needs are there that you might implement as your final project.
You can get inspiration from the projects [listed here](https://code-maven.com/programming-bootcamp-for-scientists)
and the [projects of the 2023 autumn semester](https://github.com/szabgab/wis-python-bootcamp-2023-12)
or those of [2024 spring semester](https://github.com/szabgab/wis-python-course-2024-04)
and [2024 autumn semester](https://github.com/szabgab/wis-python-course-2024-11).

The idea of the project is that you write something that is going to be useful for you beyond the course. e.g. There is some manual work in your lab and this project will automate it.
It can be also a tool to help you with your research. etc. It can also be useful in your private life. e.g. we had projects trying to register for visa applications at the USA embasy
and we also had games.

You can even take an existing project and make some valuable improvements to that project. (e.g. one project from one of the previous courses).

**How to submit your proposal?**

* Create a separate repository for the project. Its name should reflect the project: (e.g. Gene-Amplification-and-SNP-Analysis) and not the the course.
If someone looks at this repository they should see it as a real application and not "some stuff you wrote just to get the grade".

* The proposal should be the README.md file of the repository. If you need to include images or data files, those should be also included in the repository.
It should be a description that will help any future visitor of the project to understand

1. What does this project do?
1. What kind of input data it expects and what kind out output the user might expect?
1. The technicalities: How to download it, install the dependencies, run the tests, and run the project?

It would be nice if at the end of the README you mention that this was written as part of the course and link to the course repository.

We understand that the project and thus the description might evolve during the implementation. That's fine. You can update the README with the new information. In the proposal we would like to see your understanding of the project before you start implementing it.

Before you submit it for approval it is recommended that you send it to another student and ask if the description is clear. If that student has any questions then you probably will need to update the README to answer those questions so the next person won't need to ask.

Once you are ready, open an issue on our repository linking to you project to get it approved.

Once the project is approved you will implement it in the same repository. Open a new issue when you'd like the project to be graded.



### Expected workload

In addition to the lectures you will spend about 2-4 hours / week on the assignments and 20-40 hours on the project.

The actual time spent will greatly depend on your previous experience with programming in general and Python in particular.

The time you spend on the project will also depend on the availability of the data you work on.
If you pick a project that you would want to do anyway then this is basically time you would spend anyway.


### Grades

* Each assignment counts as 5% (we will have 10 of them).
* The project proposal is 15%.
* The project is 35%.

* The project is a requirement. Without that you won't get a passing grade.

### Slides

During the course I'll use some of the [slides that can be found here](https://slides.code-maven.com/python/).
These slides are publicly available and will remain on the web site after the course is over.

### Videos in English

There are [recording of this course from 3 years ago](https://code-maven.com/programming-bootcamp-for-scientists).

There are also [recordings from the 2023 autumn semester](https://github.com/szabgab/wis-python-bootcamp-2023-12).

There are also [recordings from the 2024 spring semester](https://github.com/szabgab/wis-python-course-2024-04).

You can watch those, but be also warned, this semester the order of the material will be different.

There are many more videos in my [English-language YouTube channel](https://code-maven.com/youtube).
You are invited to check them out and to follow the channel.

### Videos in Hebrew

Some of the material is also available in Hebrew. You can find them [on my website](https://he.code-maven.com/)
and in my [Hebrew-language YouTube channel](https://he.code-maven.com/youtube). You are invited to
follow that channel as well.

### Language

The default teaching language of WIS and of this course is English.

In writing please stick to English.

If and when we have one-on-one conversions I'd be happy to speak in Hebrew, Hungarian, Spanish, or Ladino as well.

### Bring your own computer!

You are expected to bring your own computer to the lectures.

### Installations

There is no need to install anything up front. We'll do that during the lectures.

### Videos

Login to [Moodle](https://feinberg.weizmann.ac.il/) and you should be able to see the video recordings on the right hand side.

## Day 1

### Plan

* Self introduction
* Overview of the course
* Programming
    * The language: [Python](https://www.python.org/)
    * 3rd party libraries on [PyPI](https://pypi.org/) e.g. [Biopython](https://biopython.org/).
    * On GitHub
* Version control
* [GitHub](https://github.com/)
* GitHub pages

### Assignment (day 1)

* [Watch](https://git.code-maven.com/creating-a-website-on-github-pages-using-markdown)
* Create web site for yourself using GitHub pages. Remember to use the repository name `USERNAME.github.io`. Get ideas from the pages of the students in the previus courses.

* Watch the 2nd video I'll publish in a few days.
* Create a separate public repository for all the assignments of the course. (e.g. call it `python-course-assignments`)
    * Create a folder called day01
    * In the folder create a program that will print "Hello World!"

Once they are ready open an issue on the GitHub repository of the course. The title of the issue should contain your full name and name of the assignment e.g. "Day1 by Foo Bar",
in case your name is Foo Bar. In the issue include the link to the site, the link to the repository of the site, and the link to the repository of the assignment.

Dead-line: March 1, 23:00


