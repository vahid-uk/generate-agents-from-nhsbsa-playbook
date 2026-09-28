# Git - NHSBSA Digital, Data and Technology Playbook - NHSBSA

Source URL: https://nhsbsa.github.io/nhsbsa-digital-playbook/development/dev-git/

## Source content

## Contents

- NHSBSA Mandatory Rules

- Git Hosting Issue Trackers

- Issue Trackers

- Commits Clean code Logical commits Commit frequency Squashing Conventional Commits

- Clean code

- Logical commits

- Commit frequency

- Squashing

- Conventional Commits

- Branching Strategy

- Merging Promoting left to right Aligning right to left Shared branches

- Promoting left to right

- Aligning right to left

- Shared branches

- Rebasing Rebase or merge Forced pushes

- Rebase or merge

- Forced pushes

- Git configuration

- Controls

- Learn more

# Git

Git is a distributed version control system used to track changes in source code. It allows developers to collaborate on projects by managing different versions of the same files, creating branches for new features, before merging changes into software releases.

Git is built on simple and elegant principles that support independent work in an offline, local environment. Git hosting providers such as Gitlab, Github and Azure enhance the collaborative experience with features such as code review, and continuous integration and deployment build pipelines.

The command line interface to Git is notoriously unintuitive with inconsistent terminiology and arcane flags that change behaviour in unexpected ways. This often leads to users either knowing just enough to get by, or becoming experts that with strong opinions on topics such as keeping a clean commit history. This page provides key guidance to teams so that they may use Git to their best advantage.

Our suggested learning resources provide additional support for beginner and expert Git users.

## NHSBSA Mandatory Rules

Teams should be self directing and adopt tools and processes to fit their circumstances, however we have these non-negotiable standards that must be adhered to:

- Project documentation All projects must document their git conventions, including their branching strategy and controls . Changes from the standard approaches defined here must be held as decision records with a rationale for any deviation.

- Main is production The main branch must always reflect the current release, running in production. Keeping main as production makes it easier to hotfix urgent changes, such as fixing zero-day exploits. Merges into main must be fast-forward only (using the flag ff-only ). This will prevent merges if there are any divergences between the commit histories of the source branch being merged and main . If main has progressed ahead of the source branch, the difference must be resolved and tested in the source branch before merging into main. This keeps the history of main clean by avoiding any complex merge commits.

- Change attribution Code changes must contain the author and issue tracker ID .

- Release by SemVer Tag Released versions of code must be identified by a Git tag on the commit that was quality assured. Release tags must follow the Semantic Versioning standard 2.0.0 . Pre-release semantic versions must not be released into production.

- Assure quality before release Before a codebase is tagged for release, it must be assured as meeting requirements: Peer review Quality assurance Testing

- Peer review

- Quality assurance

- Testing

- Binary dependencies are not held in source control Use package managers to declare dependencies, and resolve binaries within the build. Package descriptors also enable tool to check for downstream vulnerabilities and licence compliance.

## Git Hosting

The primary Git hosting provider at the NHSBSA is Gitlab.com although some teams use Github or Azure Repositories.

Access to Gitlab is controlled via Azure Entra ID and requested via Service Desk.

### Issue Trackers

Git hosting providers often integrate with issue tracking services. Use commit messages to automatically post updates or transition tickets:

- Gitlab Jira integration On Merge Request creation, a Jira ticket ID in the branch name, commit message or MR title will link the ticket to the MR

## Commits

A Commit records the changes made to files in a codebase. The message attached to a commit should clearly communicate what changed and why. A well written commit message will help people to understand a codebase, as modern IDEs can display commit information alongside each line of code.

### Clean code

Well written commit messages support clean code. For instance, they remove the motivation for these anti-patterns:

- Journal comments A log of changes written in every file.

- Attribution and bylines Adding comments with ticket number and author diverts a reader’s attention from understanding the code as a whole. In a few months time, that change is no more important than any other.

- Commented out code Leaving redundant code in the codebase, via comment blocks adds unnecessary distraction. Use the commit history if you need to revisit old code.

### Logical commits

Logical commits refers organising change into well-defined, coherent units that represent a single logical change to the codebase:

- Each commit addresses a single concern or feature

- The commit can be understood on its own without requiring context from other commits

- The changes are complete enough to not break functionality

- The commit message clearly explains what changed and why

### Commit frequency

We recommend committing regular and often.

Take care not to sacrifice logical commits by committing too frequently. If you wish to commit unfinished work, then make this clear by labelling the commit as work in progress (wip), and later squash the commits.

Note that committing updates the ‘local’ repository stored on your development machine (for example, on your laptop or VM). To update the ‘remote’ repository on the Git hosting provider, you need to ‘push’ the changes you have committed.

Changes should be pushed to the remote at least daily to serve as backup.

### Squashing

We recommend squashing commits into logical commits prior to merge downstream. This removes unneccesary commits that can confuse, providing a clean and logical git history. Use interactive rebase to take control of squashing, and the resulting commit messages.

Most Git hosting providers support squashing on merge. We recommend against this. Automating removes control from authors on the resulting commit message. There is a risk that detail is lost from the squashed commits, or too much needless information is included. There is a further risk that issue IDs are lost, removing audit.

Commits should not be squashed automatically when merging downstream and never when merging into main . Change is only allowed into main after it has been tested in a pre-production environment. Squashing will change the commit history, rendering the tests invalid.

### Conventional Commits

We recommend adopting conventional commits to structure commit messages.

```text
<
type
>
[optional scope]:
<
description
>
[optional body]

[optional footer(s)]
```

- The commit header should contain the type of change, ticket reference and a short description. Conventional commit types build Changes that affect the build system or external dependencies (example scopes: maven, npm). ci Changes to the CI configuration files and scripts (example scopes: Gitlab-CI, Azure Devops) docs Documentation only changes feat A new feature fix A bug fix perf A code change that improves performance refactor A code change that neither fixes a bug nor adds a feature style Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc). We always recommend separating formatting changes from functional changes test Adding missing tests or correcting existing tests feat: LIS-123 adds back button

The commit header should contain the type of change, ticket reference and a short description.

- build Changes that affect the build system or external dependencies (example scopes: maven, npm).

- ci Changes to the CI configuration files and scripts (example scopes: Gitlab-CI, Azure Devops)

- docs Documentation only changes

- feat A new feature

- fix A bug fix

- perf A code change that improves performance

- refactor A code change that neither fixes a bug nor adds a feature

- style Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc). We always recommend separating formatting changes from functional changes

- test Adding missing tests or correcting existing tests

```text
feat: LIS-123 adds back button
```

- The optional body should contain details of specific changes if required

The optional body should contain details of specific changes if required

- The optional footer should contain git-trailer formatted meta-information

The optional footer should contain git-trailer formatted meta-information

## Branching Strategy

A branching strategy is a set of rules to manage and organize code changes in a Git system. A strategy helps to:

- Prevent conflicts: Avoid merge conflicts that can occur when multiple people work on the same project at the same time

- Increase productivity: Allow the team to work on different features simultaneously

- Reduce version management time: Help teams to manage release of code more efficiently

There are many Git branching strategies including:

- Git-flow

- GitHub-flow

- Trunk Based Development

We recommend using our standard branching strategy , based on git-flow.

## Merging

Consider the direction of flow for code change:

- Left or Upstream is the source of change such as a feature branch

- Right or Downstream is the target of change, ultimately Production

### Promoting left to right

The normal direction of flow for change is left to right: A developer creates a feature branch to make a change. The change is promoted to a release candidate branch and then merged into the production, main branch.

- Promoting code must always be merged via a peer review process

- Ensure promoted code is clean with few, logical commits

- Favour fast forward merge over merge commits

### Aligning right to left

Often a branch of code will fall behind the downstream code on the right, especially when working in larger teams. This divergence of code should be resolved prior to promoting.

- Aligning downstream code should be merged locally

- Favour rebase over merge commit. A merge commit when aligning downstream code will result in a complicated Git graph, which is difficult to keep tidy

- Favour squashing commits to a small number before rebasing against downstream code. Fewer commits will mean fewer merge conflicts to resolve.

### Shared branches

We recommend against using shared branches between collaborators. Prefer author specific branches, with peer-reviewed merges.

- Shared branches miss the review step between collaborators

- There is increased chance of merge commits and complex Git history when pulling divergent changes. See Git configuration for controlling pull behaviour.

## Rebasing

Rebasing is a way to tidy up the Git commit history. It involves rewriting commits for a mix of purposes:

- Fixing merge conflicts: Rebasing can alter changes in a branch to avoid conflict with changes in another branch.

- Cleaning up project history: Rebasing can create a cleaner project history by combining multiple commits into one.

- Editing commit messages: Rebasing can be used to edit previous commit messages.

- Deleting or reverting commits: Rebasing can be used to delete or revert commits that are no longer necessary

Rebase needs team consensus

Rebasing will change the Git commit graph and has potential to create an inconsistent repository that is difficult to recover from. Rebase with caution and consult your professional lead if you are unsure of what you are doing.

Whenever a shared branch is rebased, the entire team must be notified. Every team member will need to reset their local branch to the rewritten remote:

e.g.

```text
git
fetch
--all
git
reset
--hard
<
branch
>
origin/
<
branch
>
```

### Rebase or merge

We recommend that teams rebase their branches against the downstream branch whenever they diverge. This provides a more streamlined and understandable git history, and simplifies squashing.

Using a merge commit from an downstream branch makes squashing and reverting change more difficult.

We also advise squashing unecessary commits before a rebase. This simplifies conflict resolution.

### Forced pushes

Sometime we need to overwrite a branch with a re-written Git history. Be very careful when force-pushing a shared branch. Ensure that every team member understands how to resolve their local repository against a force-pushed remote branch.

Use force-with-lease as a safer way to force push:

```text
git
push --force-with-lease
```

## Git configuration

Ensure your local Git configuration is correct.

- Identity Ensure that your committer identity (name and email) is the same as your Git hosting provider identity (Gitlab, Github, Azure). We endeavour to Open Source our code which will bring commit identities into the public realm. You may choose to remain anonymous by using a ‘cipher’ identity and email address.

Identity Ensure that your committer identity (name and email) is the same as your Git hosting provider identity (Gitlab, Github, Azure). We endeavour to Open Source our code which will bring commit identities into the public realm. You may choose to remain anonymous by using a ‘cipher’ identity and email address.

- Pull Avoid merge commits on pull by setting the pull.rebase configuration option: git config --global pull.rebase true

Pull Avoid merge commits on pull by setting the pull.rebase configuration option:

```text
git
config
--global
pull.rebase
true
```

- autocrlf Windows users should configure autocrlf to true to convert unix line endings (LF) to Windows on checkout and commit. Our standard is to store unix style line endings in Git. git config --global core.autocrlf true

autocrlf Windows users should configure autocrlf to true to convert unix line endings (LF) to Windows on checkout and commit. Our standard is to store unix style line endings in Git.

```text
git
config
--global
core.autocrlf
true
```

- Git alias Optimise Git usage by providing aliases to complex or frequent git commands. Suggested alias configuration: [alias] br=branch co=checkout cp=cherry-pick lg=log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)' pf=push --force-with-lease so=show --pretty='parent %Cred%p%Creset commit %Cred%h%Creset%C(yellow)%d%Creset%n%n%w(72,2,2)%s%n%n%w(72,0,0)%C(cyan)%an%Creset %Cgreen%ar%Creset'

Git alias Optimise Git usage by providing aliases to complex or frequent git commands.

```text
[alias]
  br=branch
  co=checkout
  cp=cherry-pick
  lg=log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)'
  pf=push --force-with-lease
  so=show --pretty='parent %Cred%p%Creset commit %Cred%h%Creset%C(yellow)%d%Creset%n%n%w(72,2,2)%s%n%n%w(72,0,0)%C(cyan)%an%Creset %Cgreen%ar%Creset'
```

- .gitignore Every repository must define a .gitignore file to avoid commit of build artefacts, IDE configuration and local development files. Our standard files repository contains an example covering most use cases.

.gitignore Every repository must define a .gitignore file to avoid commit of build artefacts, IDE configuration and local development files. Our standard files repository contains an example covering most use cases.

## Controls

Git repository hosting providers support adding controls on what can be done with a hosted Git repository. These must be configured to protect the branch and release process.

- Prevent unauthorised push to production and release branches

- Prevent unapproved merge of code into the release process

- Prevent non-compliant commits and branch names

- Under Settings > Repository > Protected branches : Protect named main branch, and wildcard develop* and hotfix* Allowed to merge: Developers and Maintainers Allowed to push and merge: No-one Allowed to force push: No

- Protect named main branch, and wildcard develop* and hotfix*

- Allowed to merge: Developers and Maintainers

- Allowed to push and merge: No-one

- Allowed to force push: No

- Under Settings > Repository > Branch rules : Add rule for All protected branches Add approval rule Required approvals at 1 as a minimum. Projects may choose more approvers.

- Add rule for All protected branches

- Add approval rule

- Required approvals at 1 as a minimum. Projects may choose more approvers.

- Under Settings > Repository > Push rules : Check: Reject unverified users Check: Check whether the commit author is a GitLab user Branch Name: ([A-Z]{3,4})-|develop-|hotfix-|NO-JIRA-|main)

- Check: Reject unverified users

- Check: Check whether the commit author is a GitLab user

- Branch Name: ([A-Z]{3,4})-|develop-|hotfix-|NO-JIRA-|main)

- Under Settings > Merge requests Merge method: Fast-forward merge Merge checks: Checked: Pipelines must succeed Checked: All threads must be resolved Merge request approvals Checked: Prevent approval by author Checked: Prevent editing approval rules in merge requests When a commit is added: Remove all approvals

- Merge method: Fast-forward merge

- Merge checks: Checked: Pipelines must succeed Checked: All threads must be resolved

- Checked: Pipelines must succeed

- Checked: All threads must be resolved

- Merge request approvals Checked: Prevent approval by author Checked: Prevent editing approval rules in merge requests When a commit is added: Remove all approvals

- Checked: Prevent approval by author

- Checked: Prevent editing approval rules in merge requests

- When a commit is added: Remove all approvals

## Learn more

- Official Git documentation

- NHSBSA introduction to Git

- NHSBSA Git cheatsheet

- Baeldung Git for Beginners: The Definitive Practical Guide

- Learn Git Branching

- Git Katas

- Atlassian on Git rebase

- Git immersion

## Related articles

- Git branching strategy REVIEW A branching strategy provides structure for pushing changes through to production 11 September 2026

## Git branching strategy

A branching strategy provides structure for pushing changes through to production

## Improve the playbook

If you spot anything factually incorrect with this page or have ideas for improvement, please share your suggestions.

Before you start, you will need a GitHub account . Github is an open forum where we collect feedback.

Published: 11 September 2026

Last reviewed: 20 March 2025

Next review due: 20 March 2026
