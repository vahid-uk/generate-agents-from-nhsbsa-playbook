# Peer review - NHSBSA Digital, Data and Technology Playbook - NHSBSA

Source URL: https://nhsbsa.github.io/nhsbsa-digital-playbook/development/coding-peer-review/

## Source content

## Contents

- 1. Author creates Branch

- 2. Author commits new code and pushes branch Guidelines for code changes

- Guidelines for code changes

- 3: Author creates/assigns Merge Request for review Guidelines for merge requests

- Guidelines for merge requests

- 4. Reviewer reviews code When reviewing Guidelines for reviewing code quality

- When reviewing

- Guidelines for reviewing code quality

- 5. Reviewer add (or un-resolve) comment Guidelines for comments

- Guidelines for comments

- 6. Author reviews comments

- 7. Reviewer approves code

- 8. Merge code

# Peer review

NHSBSA peer review process is mandatory

Only deviate with agreement from your Delivery Manager and Professional Lead

The high level process is:

## 1. Author creates Branch

All new code should be committed on a topic branch from the mainline production code (main).

Topic branches should follow the naming convention :

> {change-type}/{JIRA ticket number}-{dash separated human description}

{change-type}/{JIRA ticket number}-{dash separated human description}

E.g.

> feature/LISD-1782-private-pension-order-fix

feature/LISD-1782-private-pension-order-fix

## 2. Author commits new code and pushes branch

All changes for the ticket should be committed against the topic branch. It is fine to branch from this branch for experimentation, and to merge locally or in a separate review.

Branches should be pushed to gitlab no less than daily to ensure safe-keeping of code.

### Guidelines for code changes

- Keep change to a minimum The bigger the change, the longer it will take to understand and review. Large changes bring a higher risk of breaking something.

- Do one thing Avoid adding multiple functional changes in a single branch. Structure changes to allow isolated change requests

- Avoid reformatting Reformatted code can make it difficult to see functional changes. Reformatting should be done in a separate request, making clear that it only contains non-functional changes.

- Ensure the build passes Builds must pass all code quality checks.

- Tests are written Review the testing guidelines to make sure they are fit for purpose.

- Consider squashing commits Squashing commits can provide a cleaner Git history, and removes unwanted or experimental changes. Forced pushes can make it difficult for your reviewer to collaborate. Take time to keep them informed.

## 3: Author creates/assigns Merge Request for review

A Merge Request (MR) should be created in Gitlab and either:

- assign to a different person for code review or

- set as READY FOR REVIEW to allow a different person to claim

> NB: Do not use automatic MR creation in the build pipeline. These are created by the gitlab-runner user meaning it isn’t obvious who the MR came from. Furthermore, the merge commit will also belong to the MR creator and traceability is lost.

NB: Do not use automatic MR creation in the build pipeline. These are created by the gitlab-runner user meaning it isn’t obvious who the MR came from. Furthermore, the merge commit will also belong to the MR creator and traceability is lost.

Merge requests in Gitlab can be prefixed with Draft: . This is a useful way to separate ongoing work in a list of Merge Requests. They can be ignored by a reviewer until the draft status is removed.

### Guidelines for merge requests

- Update draft descriptions A quick summary of what’s left to do or why it might be on hold makes it easier to recall the current status. This is very important if a MR goes stale.

- Ensure the build passes

- Ensure the code is mergeable You should resolve any merge conflicts prior to assigning to review Sometimes code gains merge conflicts after the request is created. The Reviewer should notify the Author if this happens

- Communicate Let your reviewers know that the MR is waiting and seek acknowledgement.

## 4. Reviewer reviews code

> NB: Reviewers should never sit on an active merge request without talking to the author. If you are unable to review, seek approval to defer from the Author. The MR can then be re-assigned to another Reviewer or a deferral deadline agreed.

NB: Reviewers should never sit on an active merge request without talking to the author. If you are unable to review, seek approval to defer from the Author. The MR can then be re-assigned to another Reviewer or a deferral deadline agreed.

Code review is an important process, and should not be undertaken lightly. Unless you have been actively involved in a very minor change, do not simply browse the changes and hit merge if it ‘looks right’.

### When reviewing

- Communicate Let the author know that you are reviewing. Use the 👀 emoji against the author’s Slack message as a quick way to let them know you’re looking.

- Understand the requirement Locate and read the JIRA ticket to understand what is required. Seek clarification from the project team if needed.

- Check out code locally It can be tempting to review solely in Gitlab. This is a major cause for merging defective code.

- Build locally Include unit and/or integration tests.

- Run and verify functionality of web application/web service against requirement

- Review Sonar code quality

- Review impact of the change Do not be constrained to the specific code changes: If the changed code calls unchanged code, but that code appears faulty, consider the faulty code ‘in scope’ of review.

### Guidelines for reviewing code quality

There is no magic formula or checklist to ensure code quality, but consider the following:

- Is the code readable? Badly formatted code should be rejected

- Is the code understandable? Complex code can usually be refactored to be more simple. Partial features should only be allowed into main (production) if protected by a feature flag

- Is the code tested? Untested code should not be merged Tests must be understandable. If you don’t understand the test, you can’t be sure they are effective Its fine to add review comments to test code

- Are there any bugs? Its fine to write, commit and push new tests to illustrate a bug

- Could it be done in a better way? Talk to the Author There is often a fine line between coding style and good practice. Have a chat with the Author over more complex issues.

## 5. Reviewer add (or un-resolve) comment

Always add a descriptive comment in Gitlab for any issue found.

The reviewer should talk to the author about the contentious issues, but leave a comment regardless. Code review comments in Gitlab act as an issue tracker: If you don’t leave a comment there is a chance the issue will be forgotten.

Optionally mark the MR as WIP to clarify that the MR won’t be merged until discussions resolved.

### Guidelines for comments

- Clearly state the problem Add alternative implementation code if it helps illustrate a solution. Direct the Author to any helpful resources, such as javadoc, reference docs or articles.

- Communicate Although the Author will receive an email from Gitlab, it is helpful to notify the Author in person or via Slack for a speedy response.

## 6. Author reviews comments

Review the comments. If they are not clear, talk to the Reviewer.

- Challenge Reviewer If you disagree with the comment, talk to the reviewer, and agree a resolution

- Resolve comment Once the comment has been addressed, the Author should mark the comment as resolved

- Remove WIP status If the reviewer had tagged the MR as WIP, remove the WIP status

- Communicate Although the Reviewer will receive an email from Gitlab, it is helpful to notify the Reviewer in person or via Slack for a speedy response

## 7. Reviewer approves code

The Reviewer should approve the code, only when all comments are resolved and they approve the change.

> NB: Merged code is the shared responsibility of the Reviewer and the Author

NB: Merged code is the shared responsibility of the Reviewer and the Author

- Communicate Let the author know that you have approved. Use the ✅ emoji against the author’s Slack message as a quick way to let them know the change is approved.

## 8. Merge code

The reviewer or author may merge approved code in the mainline branch.

> NB: Merges to main branch should be ff-only. If its a develop or hotfix branch being merged you may want to disable squashing commits.

NB: Merges to main branch should be ff-only. If its a develop or hotfix branch being merged you may want to disable squashing commits.

Note that Gitlab allows you to squash commits and to remove merged branches.

## Related articles

No articles found.

## Improve the playbook

If you spot anything factually incorrect with this page or have ideas for improvement, please share your suggestions.

Before you start, you will need a GitHub account . Github is an open forum where we collect feedback.

Published: 11 September 2026

Last reviewed: 6 May 2023

Next review due: 6 May 2024
