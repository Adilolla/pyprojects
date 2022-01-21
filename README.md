# pyprojects

#All of thee projects are python projects.

### Steps to check in code and check out code
#ADDing public Key
vamsilol@Lavanya MINGW64 /
$ ssh-keygen -t rsa -b 4096 -C "adityavlolla@gmail.com"
Generating public/private rsa key pair.
Enter file in which to save the key (/c/Users/vamsilol/.ssh/id_rsa):
/c/Users/vamsilol/.ssh/id_rsa already exists.
Overwrite (y/n)? y
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /c/Users/vamsilol/.ssh/id_rsa.
Your public key has been saved in /c/Users/vamsilol/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:BtgbdBcHy1XB+uUHSPHm379kWWCmC7wSdJQxewSE4r8 adityavlolla@gmail.com
The key's randomart image is:
+---[RSA 4096]----+
|      . .oX*=+o. |
|     +...+.B...  |
|    ..+.. =..o*  |
|      .= o .o*...|
|      ..S o ...+.|
|       ... o ...*|
|        ... .  ++|
|        E.    o .|
|               .o|
+----[SHA256]-----+

vamsilol@Lavanya MINGW64 /
$



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
 
 C:\adicode\python\pyprojects>git pull
Warning: Permanently added the ECDSA host key for IP address '140.82.113.3' to the list of known hosts.
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
From github.com:Adilolla/pyprojects
   b9d97b2..31d2791  main       -> origin/main
Updating b9d97b2..31d2791
Fast-forward
 README.md | 94 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 94 insertions(+)

C:\adicode\python\pyprojects>git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

C:\adicode\python\pyprojects>git branch "develop"

C:\adicode\python\pyprojects>git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

C:\adicode\python\pyprojects>git push develop
fatal: 'develop' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.

C:\adicode\python\pyprojects>git branch
  develop
* main

C:\adicode\python\pyprojects>git push -u origin develop
Warning: Permanently added the ECDSA host key for IP address '140.82.112.4' to the list of known hosts.
Total 0 (delta 0), reused 0 (delta 0)
remote:
remote: Create a pull request for 'develop' on GitHub by visiting:
remote:      https://github.com/Adilolla/pyprojects/pull/new/develop
remote:
To github.com:Adilolla/pyprojects.git
 * [new branch]      develop -> develop
Branch 'develop' set up to track remote branch 'develop' from 'origin'.

C:\adicode\python\pyprojects>git staatus
git: 'staatus' is not a git command. See 'git --help'.

The most similar command is
        status

C:\adicode\python\pyprojects>git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

C:\adicode\python\pyprojects>git checkout develop
Switched to branch 'develop'
Your branch is up to date with 'origin/develop'.

C:\adicode\python\pyprojects>git pull
Warning: Permanently added the ECDSA host key for IP address '140.82.112.3' to the list of known hosts.
Already up to date.

C:\adicode\python\pyprojects>














