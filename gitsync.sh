#!/bin/bash
###
### GITDIFF - Check remote repository for updates. A low overhead script to 
### check if the local repository is up-to-date with the remote repository.
###

# Set the remote and branch you want to check
REMOTE="origin"
BRANCH="master"

# Check if the repository has any commits
if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    # Repository is initialized
    if git rev-parse --verify HEAD >/dev/null 2>&1; then
        # Retrieve the latest commit in the local branch
        local_commit=$(git rev-parse HEAD)
    else
        echo "No commits in the repository. Unable to compare with remote."
        exit 1
    fi
else
    echo "This directory is not a Git repository."
    exit 1
fi

# Retrieve the latest commit on the remote branch
remote_commit=$(git ls-remote $REMOTE $BRANCH | cut -f1)

# Compare the remote commit with the local commit
if [ "$remote_commit" = "$local_commit" ]; then
    echo "Local repository is up-to-date with remote."
else
    echo "Updates are available. Consider pulling the latest changes."
    # Optionally, you can automatically pull the changes
    git pull $REMOTE $BRANCH
fi
