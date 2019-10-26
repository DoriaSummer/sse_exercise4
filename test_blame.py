# Created by Wuli.Zuo a1785343
# 12/Oct/2019

import identify
from git import Repo, RemoteProgress
import os

# Function of git commands to identify VCC
def git_test_blame(local_link, fixing_commit):

    # Create repo object
    repo = Repo(local_link)

    # Reset to given commit
    repo.git.reset('--hard', fixing_commit)

    # Task 5: Compare results of different git.blame parameters
    # '-wCCC' is ignored because of the error: fatal: bad revision '–wCCC'

    parameters = ['-w', '-wM', '-wC', '-wCC']

    for parameter in parameters:

        # Create repo object
        repo = Repo(local_link)

        # Reset to given commit
        repo.git.reset('--hard', fixing_commit)

        # Frequencies of commits are calculated during Question a and b
        commits = []
        commits_count = []

        # Operate all the affected files one by one
        for file in repo.git.show('--name-only', '--format=').splitlines():
            # print("\nFile: %s" % file)
            lines = repo.git.show('-U0', file).splitlines()

            # Catch error of new added files
            try:
                file_blame_info_pre = repo.git.blame(parameter, '-f', '-e', '-t', fixing_commit + "^", file).splitlines()
            except:
                # print("%s is a new added file." % file)
                continue
            else:
                # Operate for each summary line
                for line in lines:
                    if line.startswith("@@"):
                        (start_del, length_del, start_add, length_add) = identify.analyse_diff_summary(line)

                        # Question a: identify the latest commit that modified each deleted line
                        # For each deleted lines, find latest commit
                        for i in range(start_del, start_del + length_del):
                            # print("Deleted line: %d" % i)
                            blame_info = file_blame_info_pre[i - 1]
                            target_commit = blame_info.split()[0]
                            # print("Target commit: %s" % target_commit)
                            # Count commit
                            if target_commit in commits:
                                index = commits.index(target_commit)
                                commits_count[index] += 1
                            else:
                                commits.append(target_commit)
                                commits_count.append(1)

                        # Question b: identify the latest commit that modified lines in the the smallest enclosing scope of each added line
                        # For added lines, find the smallest enclosing scope
                        # for i in range(start_add, start_add + length_add):
                            # print("Added line: %d" % i)
                        (scope_begin_line_num, scope_end_line_num) = identify.find_enclosing_scope(start_del,
                                                                                          file_blame_info_pre)
                        if not scope_begin_line_num == 0:
                            blames_info = file_blame_info_pre[scope_begin_line_num - 1: scope_end_line_num]
                            target_commit = identify.find_most_recent_commit(blames_info)
                            # print("scope in the previous commit: %d, %d" % (scope_begin_line_num, scope_end_line_num))
                        else:
                            target_commit = 'skip'
                            # print("scope in the previous commit: whole file")
                        # print("Target commit: %s" % target_commit)

                        # Count commit * length_add
                        if target_commit in commits:
                            index = commits.index(target_commit)
                            commits_count[index] += length_add
                        else:
                            commits.append(target_commit)
                            commits_count.append(length_add)

        # Find most frequently identified commit as the VCC
        vcc = commits[commits_count.index(max(commits_count))]
        print("VCC with Parameter %s is: %s" % (parameter, vcc))

# main

class Progress(RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        print(self._cur_line)

# Case 1
remote_link = "https://github.com/spring-projects/spring-amqp"
local_link = "../spring-amqp"
if not os.path.isdir(local_link):
    Repo.clone_from(remote_link, local_link, progress=Progress())
fixing_commit = "444b74e95bb299af5e23ebf006fbb45d574fb95"
print("\nOperation of repo: %s" % (remote_link))
git_test_blame(local_link, fixing_commit)

# Case 2
remote_link = "https://github.com/apache/pdfbox"
local_link = "../pdfbox"
if not os.path.isdir(local_link):
    Repo.clone_from(remote_link, local_link, progress=Progress())
fixing_commit = "4fa98533358c106522cd1bfe4cd9be2532af852"
print("\nOperation of repo: %s" % (remote_link))
git_test_blame(local_link, fixing_commit)

# Case 3
remote_link = "https://github.com/apache/tomcat80"
local_link = "../tomcat80"
if not os.path.isdir(local_link):
    Repo.clone_from(remote_link, local_link, progress=Progress())
fixing_commit = "ec10b8c785d1db91fe58946436f854dde04410fd"
print("\nOperation of repo: %s" % (remote_link))
git_test_blame(local_link, fixing_commit)

# Case 4
remote_link = "https://github.com/apache/tomcat"
local_link = "../tomcat"
if not os.path.isdir(local_link):
    Repo.clone_from(remote_link, local_link, progress=Progress())
fixing_commit = "e246e5fc13307da0a5d3bbf860d64d97be1c40f8"
print("\nOperation of repo: %s" % (remote_link))
git_test_blame(local_link, fixing_commit)

# Case 5
remote_link = "https://github.com/apache/ignite"
local_link = "../ignite"
if not os.path.isdir(local_link):
    Repo.clone_from(remote_link, local_link, progress=Progress())
fixing_commit = "340569b8f4e14a4cb61a9407ed2d9aa4a20bdf49"
print("\nOperation of repo: %s" % (remote_link))
git_test_blame(local_link, fixing_commit)

# Case 6
remote_link = "https://github.com/apache/cxf"
local_link = "../cxf"
if not os.path.isdir(local_link):
    Repo.clone_from(remote_link, local_link, progress=Progress())
fixing_commit = "8f4799b5bc5ed0fe62d6e018c45d960e3652373e"
print("\nOperation of repo: %s" % (remote_link))
git_test_blame(local_link, fixing_commit)