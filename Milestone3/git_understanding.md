Tasks:

In a Git repository, a Pull Request (PR) is a request to merge changes from one branch into another. Before merging code changes into the main project, developers can examine, discuss, and propose changes. A pull request is used for code review before merging, suggestion for improvements, tracking changes, allow automated tests and bug fixes.

When writing code, a Pull Request facilitates teamwork. It enables team members to examine modifications before to merging prevents errors. It enhances Code Quality. PRs document the reasons behind modifications. Before merging, automated tests can look for errors.

A well-structured PR is easy to read and understand. It includes a descriptive title, description, small changes that easy to review, tests and links to related issues.

i) Discussions are vital as developers provide feedback to make the code better.
ii) Changes must be explained: Provide an explanation for the adjustments they made.
iii) Testing Is Important: Verify that the new code has been properly tested.
iv) Small PRs are easier to review.

I created a new branch with name Branch1. I did a small change in my README.md file (added one extra comment). Added, committed and pushed to the Github. Added a meaningful title and description and merged the PR request to the main branch. Deleted the new branch.

Tasks:

Best practices for writing commit messages:
1. Clear and concise message.
2. Meaningful and descriptive message.
3. Use common prefixes and subject short.
4. Reference issues.

1. A good commit message should be clear, concise, structured format using type and description.
2. A clear commit message helps to review the code quickly. 
   It improves debugging process as if any issues arise, it's easier to track the origin of the 
   issue.
   It also enhance the corrdination between team members. By using a good commit 
   message , the team members knows what is being worked on, to minimize the conflicts.
3. A poor commit message makes it difficult to track the changes. It includes the wastage of time. It increases the merge conflicts as multiple developers works on the same part of the code. That's why, the bad commit message makes the context of changes, a bad history. 

Tasks:

Reflect on why teams use branches instead of pushing directly to main in git_understanding.md:

Teams use branches to prevent the codebase for the entire application. It allows us to review the code to find bugs before merging. Different features can work on different branches. Testing can be done to check if the changes is working. With branches, the merge conflicts is easier to handle.

1. The codebase can introduce conflicts if someone's changes includes bugs.
    It reduces the chances to review the code, testing and improvements.

2. i) Each developer can create their own branch and work independently on a particular 
      feature.
   ii) By creating pull requests, the code can be reviewed before merging the changes to 
       the main branch, which allows to find bugs and better feedback.
  iii) With the help pf branches, it's easier to track the history between different features or 
       fixes.

3. If two people edit the same file on different branches, the merge conflict will occur. Git 
   tries to merge the changes but if the git can't resolve it automatically, developers have 
   to manually resolve the conflict.

   Tasks:

1. Difference between staging and committing:
Staging: This is the stage where the changes are ready to commit. In this stage, we can review our changes, modify files or not to commit the changes. For example: git add <file name>
Committing: is the process of saving the changes to the local repository. The commit message includes a unique id and the information about the changes. For example: git commit -m <commit message>. The changes will be saved after committing in the git repository. 

2. Git separate these two steps because it gives more control over commit process. 
   Staging allows to review the changes before it permanently saved to the repository. You 
   can select the file which changes you want to commit. It brings flexibility in commit 
   process.

3. We can stage the changes without committing to commit them separately. If we are 
    working on two different changes in the same file, we can stage one at a time and 
    commit instead of all changes at a time. It saves the progress without committing. we 
    can return later to commit the staged changes. It helps to review the code and 
    enhances collaboration. 


Git Bisect: 

Tasks:

1. The main purpose of git bisect is to find a commit that is causing a bug by performing a binary search thorugh the commit history. It is useful when we have a large commit history and need to find which commit is introducing a bug. Git bisect automates the process of checking different commit except manually checking each commit to find a bug.

2. Test scenario: 
   I already have few commits while i pushed my .md files to remote repository. I have 
   created a bug in one of the files. I did a simple modification in the file and used git 
   bisect to check for bad commit. And it works! Attached the screenshot. I tried to attach 
   but not sure if it is visible or not.

[Git Bisect.docx](https://github.com/user-attachments/files/19467082/Git.Bisect.docx)

3. 
   i) Git Bisect can be used when there is an issue or something is broken or any feature is 
      not working and it was working before. But we are not sure in which commit it has a 
      bug. On that time, git bisect can be used.
   ii) A codebase with various commit changes and using multiple branches can create a bug in the commit.

4. Comparison with manually reviewing commits:
    i) It saves the time and effort.
    ii) It narrows down the search.
    iii) It's an automated process and avoids any missing commits.


Git commands:

Reflections:

1. git checkout main -- <file>
    This command is used if let's see i have commit few or one commit change in my 
    branch but i don't want to that change to be added so i can get the file from main 
    branch withour these commit changes and can work on it.

2. git cherry-pick <commit>
    This command is used if we had few commit changes in our new branch and we only 
    want specific commit change to apply then we can use this command to apply specific 
    change not all of the commit changes.

3. git log command
    Git log command is useful if we want to see all the commit history in our branch.

4. git blame <file>
    This command will tell who has modified the file or who did the last changes in the file 
    and when it is done.   


I like the usage of all the commands. These all commands has their own purpose to use which is very enlightening to use in a large projects.