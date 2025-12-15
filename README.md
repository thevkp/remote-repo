# remote-repo

This repository was created to demonstrate the difference between GitHub repositories
that are initialized with a README file and those that are created empty.

When a GitHub repository is created **without a README**, cloning it results in an
**empty repository with no commits**. In this state, the default branch (usually `main`)
exists only as an *unborn branch*, meaning there is no commit history yet and Git cannot
create or track additional branches until the first commit is made.

When a GitHub repository is created **with a README file**, GitHub automatically creates
the first commit on the default branch (`main`). This initializes the repository, making
the `main` branch real and immediately allowing developers to create new branches and
begin working using standard Git workflows.
