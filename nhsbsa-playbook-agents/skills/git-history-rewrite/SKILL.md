# Git History Rewriting

Destructive history rewriting is exceptional and must be carefully controlled.

Before rewriting shared history:

- consult the professional lead
- consult Information Security/Security Operations
- assess all affected branches
- communicate with contributors and affected parties
- raise the required security incident where applicable
- create a safe backup
- script the rewrite
- peer review the script
- perform a dry run on a fresh clone
- verify the resulting history
- force-push all required branches and tags only when authorised
- require contributors to re-clone after the production rewrite

Use `git-filter-repo` for history rewriting.

Do not use obsolete `git filter-branch` or BFG for this process.

Do not use this procedure for normal topic-branch squashing or rebasing.

Source:
https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-git-rewrite-history/
