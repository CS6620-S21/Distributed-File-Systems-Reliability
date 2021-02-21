# Distributed-File-Systems-Reliability

## 1. Project Background
Distributed storage systems are a fundamental building block of any modern scaling computing infrastructure, such 
as in clouds, scientific computing, or next-generation data centers. This is ultimately where most of the data resides, 
so the reliability of distributed file systems in the face of failures is critical. However, unlike local file systems, 
which have many tools and frameworks for testing, there are (still) no standard frameworks for evaluating the reliability 
of distributed file systems and their unique failure modes, like node and network failures! This not only means that each 
system must implement their own tests, but also that it is difficult to compare the reliability of multiple distributed 
file systems or evaluate their reliability from a third party’s perspective.

## 2. Goals: 
Design and implement a framework for basic failure testing of distributed file systems, which could be applied to 
Ultimate goal of the project is to test different use cases for MooseFS filesystem and generalize them for few other Filesystems. 
The overall testing framework would programmatically create and set up virtual machines (VMs) using Ansible Playbooks and 
Terraform Plans for testing, run experiments, simulate node failures (e.g., terminating one or more VMs), verify the 
file system, destroy unneeded VMs, and repeat.

## 3. Users/Personas Of The Project:
- Admins and file system developers of projects or which are either forked or a variants of the MooseFS Distributed 
filesystem can consider the approach taken and generalize and automate reliability tasks by implementing an automation 
framework which will enable them to improve upon the reliability of their implementation. For example admins of LizardFS
- Production engineers who want to assess the reliability of a the related distributed file Systems by following the
methodologies adopted here.

## 3. Scope and Features Of The Project:
- The overall framework that will set up and tear down VMs, run experiments, and simulate failures.
- A set of experiments, such as writing to a large file, simulating a power failure (instantly rebooting all VMs), and 
then after they come back up, verifying that no data was lost.
- An interface with plugins for different distributed file systems. The primary goal for this project is to develop a 
reliability/failure-inducing framework for distributed filesystem that is focused on node failures. 
Stretch goals, if time allows, include:
    - Injection of block corruptions and errors on the local VMs
    - Simulate network failures
    - Performance testing specific to distributed filesystems.


## 4. Solution Concept
 
## 5. Acceptance criteria
A setup which can validate the reliability of any given Distributed File System

## 6. Release Planning:
Currently asked us to learn Ansible, Terraform and MooseFS.
Will add front end using Django if having spare time.

