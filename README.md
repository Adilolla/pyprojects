# pyprojects

#All of thee projects are python projects.

### Steps to check in code and check out code


C:\adicode\python>git clone git@github.com:Adilolla/pyprojects.git
Cloning into 'pyprojects'...
The authenticity of host 'github.com (140.82.114.3)' can't be established.
ECDSA key fingerprint is SHA256:p2QAMXNIC1TJYWeIOttrVc98/R1BUFWu3/LiyKgUfQM.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'github.com,140.82.114.3' (ECDSA) to the list of known hosts.
remote: Enumerating objects: 6, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 6 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (6/6), done.

C:\adicode\python>git status
fatal: Not a git repository (or any of the parent directories): .git

C:\adicode\python>dir
 Volume in drive C has no label.
 Volume Serial Number is 8C79-847B

 Directory of C:\adicode\python

01/09/2022  08:44 PM    <DIR>          .
01/09/2022  08:44 PM    <DIR>          ..
01/09/2022  08:50 PM    <DIR>          pyprojects
               0 File(s)              0 bytes
               3 Dir(s)  263,327,252,480 bytes free

C:\adicode\python>cd pyprojects

C:\adicode\python>cd pyprojects

C:\adicode\python\pyprojects>git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        firstpy/

nothing added to commit but untracked files present (use "git add" to track)

C:\adicode\python\pyprojects>git add .
warning: LF will be replaced by CRLF in firstpy/first.py.
The file will have its original line endings in your working directory.

C:\adicode\python\pyprojects>git commit

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'vamsilol@Lavanya.(none)')

C:\adicode\python\pyprojects># Online Python compiler (interpreter) to run Python online.# Write Python 3 code in this online editor and run it.a=7b=5print("the total of
'#' is not recognized as an internal or external command,
operable program or batch file.

C:\adicode\python\pyprojects>git config --global user.email "adityavlolla@gmail.com"

C:\adicode\python\pyprojects>git commit
Aborting commit due to empty commit message.

C:\adicode\python\pyprojects>git commit "first changes"
error: pathspec 'first changes' did not match any file(s) known to git.

C:\adicode\python\pyprojects>git commit -m "my changes"
[main b9d97b2] my changes
 1 file changed, 5 insertions(+)
 create mode 100644 firstpy/first.py

C:\adicode\python\pyprojects>git push
Warning: Permanently added the ECDSA host key for IP address '140.82.113.4' to the list of known hosts.
Counting objects: 4, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 450 bytes | 450.00 KiB/s, done.
Total 4 (delta 0), reused 0 (delta 0)
To github.com:Adilolla/pyprojects.git
   d897d24..b9d97b2  main -> main

C:\adicode\python\pyprojects>


