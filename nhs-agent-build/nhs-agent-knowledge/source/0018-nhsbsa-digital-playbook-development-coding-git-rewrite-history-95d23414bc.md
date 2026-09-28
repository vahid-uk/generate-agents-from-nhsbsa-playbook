# Rewriting Git history - NHSBSA Digital, Data and Technology Playbook - NHSBSA

Source URL: https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-git-rewrite-history/

## Source content

## Contents

- When to rewrite history

- Assess the impact

- Raise an incident

- Skills

- Execution steps

# Rewriting Git history

Proceed with caution

Rewriting history will change the Git commit graph and has a high potential to create a mess of a repository. Incorrect or unmanaged use of tools can lead to an inconsistent Git repository which is difficult to recover from. Proceed with caution and follow this guidance to protect your project from unintended consequences.

Consult with your professional lead and security operations before any rewrite activity.

This guidance does not cover normal development activities such as squashing commits on a topic branch, or rebasing prior to merge. These branches are not shared widely and sensitive data is not involved. Collaborative Git practices should be agreed with your team.

## When to rewrite history

Many secrets can be revoked by deleting the secret and regenerating a new one. Applications must then be reconfigured with the new value. This is the preferred way to deal with secrets in code. The NHSBSA Gitleaks project includes links to the various secrets providers, with documentation on creating and revoking secrets. See our guidance on ignoring revoked secrets in Gitleaks .

Some sensitive information cannot be revoked, and should be removed from the Git history when open sourcing.

Consider:

## Assess the impact

Consider all branches, including main , develop and release , in scope of rewrite. These branches are shared widely, especially when published in the open.

Assess who will be impacted by publishing destructive changes, including:

## Raise an incident

Raise a security incident with the Information Security team when you discover secrets committed to a repository. They will ensure you have documented approval from these stakeholders, prior to any destructive rewrite:

- Information Governance

- Security Operations

- Architecture

- Software Development

If the impact extends to external collaborators and the general public, consult with the Communications team.

## Skills

Contributors who rewrite history must have the appropriate skills:

- Git concepts It’s important to understand The Git directed acyclic graph, how commits are immutable and must be replaced. That branches and annotations must be assigned to the newly created commits and their children. That a rewritten git repository will diverge from the original clone, and how this can cause damage if merged back into the original.

- The Git directed acyclic graph, how commits are immutable and must be replaced.

- That branches and annotations must be assigned to the newly created commits and their children.

- That a rewritten git repository will diverge from the original clone, and how this can cause damage if merged back into the original.

- Git commands You should be very comfortable with these commands and understand what they do: git log A key skill is determining if a rewrite is successful. Git log is invaluable for this, as you can export logs before and after and compare the output. --all --oneline --graph --abbrev-commit --format -sne git shortlog Shortlog is use to extract data for authors, in order to anonymise. -sne git push You must understand how to push the rewritten repository and replace all commits, branches, tags. The remote repository should not contain any orphan commits, or any references pointing to old commits. --force --tags

- git log A key skill is determining if a rewrite is successful. Git log is invaluable for this, as you can export logs before and after and compare the output. --all --oneline --graph --abbrev-commit --format -sne

- --all

- --oneline

- --graph

- --abbrev-commit

- --format

- -sne

- git shortlog Shortlog is use to extract data for authors, in order to anonymise. -sne

- -sne

- git push You must understand how to push the rewritten repository and replace all commits, branches, tags. The remote repository should not contain any orphan commits, or any references pointing to old commits. --force --tags

- --force

- --tags

- Git filter-repo git-filter-repo is the recommended tool for rewriting Git history. Do not use outdated tools such as BFG or git-filter-branch. The key commands to cover most cases are: --analyze --mailmap --replace-text

- --analyze

- --mailmap

- --replace-text

- Bash scripting You will write a single script to perform all rewrite steps on a clean clone of the repository.

This article provides an in-depth guide to removing secrets from Git history by rewriting history:

- Git Clean, Git Remove file from commit - Cheatsheet

## Execution steps

- Create a private subgroup called backup Fork the code repository here for safekeeping. The backup may be deleted at a later date

- Create a private subgroup called git-rewrite . Fork the code repository here. This will be used to develop, test and review the rewrite. Rewrites to this repository must be performed as a single, scripted action and pushed only once. Any subsequent rewrites must be performed on fresh forks from the original. This ensures the rewrite is clean and repeatable.

- Fork the template project git-rewrite-scripts under the git-rewrite subgroup This will contain the scripted actions to rewrite history. It is important to script the actions, so that a peer may review and verify correctness. The scripted actions and associated resources will contain sensitive data and must be kept private. It will serve as an audit history if required.

- Develop the rewrite script and peer review with a Merge Request See the template project for guidance on script writing.

- Dry run Local development should stop. Consult with team to ensure all local branches are pushed to the production repository. Create a fresh fork of the repository in git-rewrite folder. Rewrites must be performed on a fresh clone of the forked repository Apply scripted rewrites Add remote origin as rewrite will remove that relationship Configure protected branches to allow force push Force push the repository git push --all --force Force push the tags git push --tags --force Configure protected branches to disallow force push Consult with team to assure all is as expected

- Local development should stop.

- Consult with team to ensure all local branches are pushed to the production repository.

- Create a fresh fork of the repository in git-rewrite folder.

- Rewrites must be performed on a fresh clone of the forked repository

- Apply scripted rewrites

- Add remote origin as rewrite will remove that relationship

- Configure protected branches to allow force push

- Force push the repository git push --all --force

- Force push the tags git push --tags --force

- Configure protected branches to disallow force push

- Consult with team to assure all is as expected

- Apply the rewrite Repeat the clone, rewrite, push, review, but this time on the production repository

All team members must re-clone from the rewritten remote

Old clones should be discarded. Pulling a rewritten remote into the original can create a mess that is very difficult to recover from.

## Improve the playbook

If you spot anything factually incorrect with this page or have ideas for improvement, please share your suggestions.

Before you start, you will need a GitHub account . Github is an open forum where we collect feedback.

Published: 11 September 2026

Last reviewed: 15 May 2023

Next review due: 15 May 2024
