# Coding - NHSBSA Digital, Data and Technology Playbook - NHSBSA

Source URL: https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding/

## Source content

## Contents

- Coding principles

- Software Development Patterns

- Clean code

- Code smells and refactoring

- 12 Factor App

- References

# Coding

> Any fool can write code that a computer can understand. Good programmers write code that humans can understand. Martin Fowler

Any fool can write code that a computer can understand. Good programmers write code that humans can understand. Martin Fowler

This page highlights some key advice when coding.

## Coding principles

There are many principles that we should keep in mind when writing code. You can read about many of these on the Principles wiki . Some principles of note:

- Don’t Repeat Yourself

- Keep It Simple Stupid

- Murphy’s Law - Design for Errors

- Postel’s Law - Be conservative in what you do, be liberal in what you accept from others

- Principle of least privilege

- SOLID principles comprising: Single Responsibility Principle Open Closed Principle Liskov Substitution Principle Interface Segregation Principle Dependency Inversion Principle

- Single Responsibility Principle

- Open Closed Principle

- Liskov Substitution Principle

- Interface Segregation Principle

- Dependency Inversion Principle

## Software Development Patterns

Design patterns are common approaches to solving common problems in software development. The book Design Patterns: Elements of Reusable Object-Oriented Software by the Gang of Four describes the original patterns they identified. They are divided into creational, structural and behavioural patterns and should be understood and used where appropriate.

The Refactoring Guru website covers design patterns in an engaging format.

## Clean code

> “Clean code is code that has been taken care of. Someone has taken the time to keep it simple and orderly. They have paid appropriate attention to details. They have cared.” ― Robert C. Martin

“Clean code is code that has been taken care of. Someone has taken the time to keep it simple and orderly. They have paid appropriate attention to details. They have cared.” ― Robert C. Martin

We advise all developers to read the seminal book Clean Code: A Handbook of Agile Software Craftsmanship by Robert C. Martin.

To get an idea of the scope of Robert Martin’s book, take a look at the chapter headings .

## Code smells and refactoring

Kent Beck coined the term code smell to refer to problems with code that are easy to spot, easy to fix but can signify more serious underlying problems. Martin Fowler described a set of standard code smells and associated patterns to refactor code and fix them.

We advise all developers to read Martin Fowler’s book Refactoring: Improving the Design of Existing Code .

Alternatively, visit the Refactoring website that describes code smells and refactors.

## 12 Factor App

Production application code should be written according to principles defined in The 12 Factor App :

- Codebase - One codebase tracked in revision control, many deploys

- Dependencies - Explicitly declare and isolate dependencies

- Config - Store config in the environment

- Backing services - Treat backing services as attached resources

- Build, release, run - Strictly separate build and run stages

- Processes - Execute the app as one or more stateless processes

- Port binding - Export services via port binding

- Concurrency - Scale out via the process model

- Disposability - Maximize robustness with fast startup and graceful shutdown

- Dev/prod parity - Keep development, staging, and production as similar as possible

- Logs - Treat logs as event streams

- Admin processes - Run admin/management tasks as one-off processes

## References

- Principles wiki

- Design Patterns: Elements of Reusable Object-Oriented Software

- Clean Code: A Handbook of Agile Software Craftsmanship

- Refactoring: Improving the Design of Existing Code

- Refactoring Guru

- 12 Factor App

## Improve the playbook

If you spot anything factually incorrect with this page or have ideas for improvement, please share your suggestions.

Before you start, you will need a GitHub account . Github is an open forum where we collect feedback.

Published: 6 May 2023

Last reviewed: 6 May 2023

Next review due: 6 May 2024
