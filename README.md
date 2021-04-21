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
the ultimate goal of the project, which is to test different use cases for MooseFS filesystem and generalize them for few other 
Filesystems. The overall testing framework would programmatically create and set up virtual machines (VMs) for Master 
Server, Metaloggers, multiple Chunkservers(ideally 50-60), and Client Servers using Ansible Playbooks and Terraform Plans 
for testing, run experiments, simulate node failures (e.g., terminating one or more VMs), verify the file system, destroy 
unneeded VMs, and repeat.
Automate configuration and infra setup
Develop Testing framework for targeted DFS
APIs for interacting with the framework

## 3. Users/Personas Of The Project:
- Admins and file system developers of projects which are either forked or a variants of the MooseFS Distributed 
filesystem, can consider the approach taken and generalize and automate reliability tasks by implementing an automation 
framework which will enable them to improve upon the reliability of their implementation. For example admins of LizardFS.
- Production engineers who want to assess the reliability of a the related distributed file Systems by following the
methodologies adopted here.
- Software developers and QA personnel working on developing file systems by utilizing the provided approach.

## 3. Scope and Features Of The Project:
- The overall framework that will set up and tear down VMs, run experiments, and simulate failures.
- A set of experiments, such as writing to a large file, simulating a power failure (instantly rebooting all VMs), and 
then after they come back up, verifying that no data was lost.
- An interface with plugins for different distributed file systems. The primary goal for this project is to develop a 
reliability/failure-inducing framework for distributed filesystem that is focused on node failures. 
Stretch goals, if time allows, include:
    - Injection of block corruptions and errors on the local VMs;
    - Simulate network failures;
    - Performance testing specific to distributed filesystems.

## 4. Solution Concept
Note: Since their are many different types of distributed file system the idea here is to hide the steps taken behind clean 
interfaces, and thus testing different file systems would require developing different ansible playbooks which are an 
of these interfaces.
#### Architecture Overview
![arch diagram](https://user-images.githubusercontent.com/52186552/112475253-990a2600-8d3e-11eb-8964-f4080c9e27eb.jpg)
The user connect to the management VM and use it as the workflow engine, drive the testing routine through Python:
- (1-2)Utilize Terraform to create and start VMs on openStack.
- (3-4)Utilize Ansible Playbook to configure environment and install MooseFS servers(Master, Metalogger, Chunkserver, Client) on corresponding VM. Start the servers after creation.
- (5-6)Use SSH/SCP/SFTP to connect to the client VM(s) and run the testing scripts to create some file with contents on Client server.
- (7)Through Terraform, Reboot/destroy MooseFS server(s).
- (8)SSH to the client VM to check the status/content of the testing files.
- (9)Destroy all the VMs through Terraform.

#### Workflow API 
##### Architecture
- Management VM
    - Driver of various tests
    - Workflow Engine
- MooseFS Server VM
    - Master Server VM
    - Chunk Server VM
    - Metalogger Server VM
- MooseFS Client VM
    - Runs workflow commands to interact with MooseFS Master and Chunk Server VMs
    - Checks for file corruption
![10251618967832_ pic_hd](https://user-images.githubusercontent.com/52186552/115482930-66582e00-a215-11eb-8809-3ef7ad2e3d02.jpg)

##### Driver Program Class Diagram
![10311618973062_ pic_hd](https://user-images.githubusercontent.com/52186552/115489354-b210d480-a221-11eb-8fb6-2113b386ffab.jpg)

#### Environment Configuration on Management VM
![10261618968000_ pic](https://user-images.githubusercontent.com/52186552/115483193-ef6f6500-a215-11eb-94c4-3a0bd9d95114.jpg)
- Terraform
    - Terraform plays the part of creating and maintaining the infrastructure 
    - Successfully connected to the OpenStack platform and programmatically provision VMs using terraform
    - A Python layer over Terraform, which interacts with the Terraform to create the required infrastructure
- Ansible
![10231618956435_ pic_hd](https://user-images.githubusercontent.com/52186552/115470503-0acd7680-a1fc-11eb-89bb-ba07b4c5d2a8.jpg)
    - Implemented Ansible Playbook for setting up different MooseFS servers.
    - Automated the setup of Master Server, Metalogger, Chunkserver, and Client server.

#### Five different failure scenarios
![10271618972754_ pic_hd](https://user-images.githubusercontent.com/52186552/115488955-fa7bc280-a220-11eb-8a52-d440ea7309a3.jpg)
![10281618972765_ pic_hd](https://user-images.githubusercontent.com/52186552/115488975-049dc100-a221-11eb-9094-f655b1a85910.jpg)
![10291618972775_ pic_hd](https://user-images.githubusercontent.com/52186552/115489006-12ebdd00-a221-11eb-855a-5390b2a440ae.jpg)
![10301618972789_ pic_hd](https://user-images.githubusercontent.com/52186552/115489038-1e3f0880-a221-11eb-9219-4e9411fac807.jpg)
 
## 5. Acceptance criteria
- Teraform Scripts should be able to create VMs on demand in MOC.
- Ansible playbooks should be able to setup the VMs through automation by installing & configuring different file systems.
- Ansible playbooks should be able to test different file systems.
- Thoroughly testing the MooseFS distributed file system and figuring out what are the possible interfaces required such an assessment.
- In the later phases we will try to provide implementation of these interface for other file systems and thus provide 
a guideline or a general approach to be taken to test any Distributed File System.

## 6. Release Planning:

#### Sprint 1 (12 Feb 2021 to 26 Feb 2021)
- Due for Week 1:
    - Learning Ansible & Installing it on VMs(VirtualBox VMs)
    - Learning Terraform & Experimenting on AWS VMs
    - Set up MooseFS on our local machine (with VirtualBox VMs)
- Due for Week 2:
    - Setting up Ansible Master Control node on MOC VM
    - Learning Terraform Experimenting on MOC
    - Set up MooseFS manually on MOC

#### Sprint 2 (26 Feb 2021 to 12 Mar 2021)
- Design the project architecture
- Connect to the MOC and programmatically provision VMs using terraform
- Set up Ansible architecture and VM environment
- Automate MooseFS installation on MOC using Ansible Playbook

#### Sprint 3 (15 Mar 2021 to 27 Mar 2021)
- Enhance Terraform, Ansible, and SSH in Python Driver Program
- Design failure scenarios

#### Sprint 4 (29 Mar 2021 to 10 Apr 2021)
- Developed 4 end to end test scenarios for testing the MooseFS file system.
- Integrated the test scenarios with python main driver to create a test-harness

#### Retrospective
- Sprints Running really well
    - Achieved the sprint goal and overall project deliverables.
    - Useful having full team + mentor on MS Teams
    - Team willing to adjust schedule ad-hoc incredibly helpful

- Major Hiccups
    - Installation of  MooseFS on CentOS 
    - Switching from Java to Python after the 2nd Sprint.
    - Less features available on Terraform provider for Openstack as compared to AWS or Azure.

#### Stretch Goals
- Implement additional end to end test scenarios.
- Abstract the code to support multiple providers like AWS, Azure etc.
- Provide Web APIs.

The further releases of application are not fixed yet for a particular date and are dependent on evaluation results 
from experiments being conducted for the project.



