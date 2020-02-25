Title: Deploying a Docker Container to Digital Ocean with sshfs
Date: 2020-02-21 00:00
Modified: 2020-02-25 11:57
Category: Web Apps
Tags: configuration, make, deployment
Slug: digital-ocean
Status: published

In this post I'll talk about the way I set up the directory structure for my data science bootcamp capstone project, and how I mounted my droplet in my local file system in order to deploy my web application. I also used of a couple of makefiles so I didn't have to keep re-typing the same long shell commands in the terminal and I'll explain how the that works too.

![Broccoli directory structure]({static}/images/directory-structure.png)



### Links

* [https://www.gnu.org/software/make/](https://www.gnu.org/software/make/)