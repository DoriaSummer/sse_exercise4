# Created by Wuli.Zuo a1785343
# 26/Oct/2019

from git import Repo
import re

# Function of git commands to compare two commits
def git_compare(local_link, fixing_commit, vcc):
    # Create repo object
    repo = Repo(local_link)

    # Affected files of the fixing commit
    files_fix = repo.git.show('--name-only', '--format=', fixing_commit).splitlines()
    print("3.(d) Affected files in the fixing commit: %d" % len(files_fix))
    for file in files_fix:
         print("      %s" % (file))

    # Is the current VCC an initial commit?
    try:
        repo.git.show('--name-only', '--format=', vcc+"~")
    except:
        print("4.(a) The current VCC is an initial commit.")
    else:
        print("4.(a) Previous commit of the VCC found, the current VCC is not an initial commit.")

    # Is the same developer? Their experience?
    vcc_author = repo.git.log(-1, '--format=%aN', vcc).splitlines()[0]
    commits_time = len(re.findall(vcc_author,repo.git.log('--format=%aN')))
    print("4.(b) Developer(s): ")
    print("      The developer of the VCC: %s, Number of commits has made: %d" % (vcc_author, commits_time))
    fixing_author = repo.git.log(-1, '--format=%aN', fixing_commit).splitlines()[0]
    commits_time = len(re.findall(fixing_author, repo.git.log('--format=%aN')))
    print("      The developer of the fixing commit: %s, Number of commits has made: %d" % (fixing_author, commits_time))
    if vcc_author == fixing_author:
        print("      --> The same developer.")
    else:
        print("      --> Different developers.")

    # Number of days between two commit
    vcc_time = repo.git.log(-1, '--format=%ct', vcc).splitlines()[0]
    fixing_time = repo.git.log(-1, '--format=%ct', fixing_commit).splitlines()[0]
    # convert unit from seconds to days
    days = (float(fixing_time) - float(vcc_time)) / (60 * 60 * 24)
    print("4.(c) The number of days between the VCC and the fixing commit: %.2f" % days)

    if days <=1:
        print("      The VCC is fixed immediately.")
    else:
        print("      The VCC is not fixed immediately.")

    # Output 10 commits after the VCC
    # print(vcc_time)
    commits_after = repo.git.log('--format=oneline', '--reverse', '--after=' + str(int(vcc_time)+1)).splitlines()[0:10]
    print("4.(d) Commits after the VCC: ")
    for commit in commits_after:
        print("      %s" % commit)