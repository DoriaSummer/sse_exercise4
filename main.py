# Created by Wuli.Zuo a1785343
# 26/Oct/2019

import compare
import identify
import test_blame

from git import Repo, RemoteProgress
import os

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
print("\nAnalyse repo: %s\nfixing commit: %s" % (remote_link, fixing_commit))
vcc = identify.git_identify(local_link, fixing_commit)
print("3.(e) VCC: %s" % vcc)
compare.git_compare(local_link, fixing_commit, vcc)
# test_blame.git_test_blame(local_link, fixing_commit)

# Case 2
remote_link = "https://github.com/apache/pdfbox"
local_link = "../pdfbox"
if not os.path.isdir(local_link):
    Repo.clone_from(remote_link, local_link, progress=Progress())
fixing_commit = "4fa98533358c106522cd1bfe4cd9be2532af852"
print("\nAnalyse repo: %s\nfixing commit: %s" % (remote_link, fixing_commit))
vcc = identify.git_identify(local_link, fixing_commit)
print("3.(e) VCC: %s" % vcc)
compare.git_compare(local_link, fixing_commit, vcc)
# test_blame.git_test_blame(local_link, fixing_commit)

# Case 3
remote_link = "https://github.com/apache/tomcat80"
local_link = "../tomcat80"
if not os.path.isdir(local_link):
    Repo.clone_from(remote_link, local_link, progress=Progress())
fixing_commit = "ec10b8c785d1db91fe58946436f854dde04410fd"
print("\nAnalyse repo: %s\nfixing commit: %s" % (remote_link, fixing_commit))
vcc = identify.git_identify(local_link, fixing_commit)
print("3.(e) VCC: %s" % vcc)
compare.git_compare(local_link, fixing_commit, vcc)
# test_blame.git_test_blame(local_link, fixing_commit)

# Case 4
remote_link = "https://github.com/apache/tomcat"
local_link = "../tomcat"
if not os.path.isdir(local_link):
    Repo.clone_from(remote_link, local_link, progress=Progress())
fixing_commit = "e246e5fc13307da0a5d3bbf860d64d97be1c40f8"
print("\nAnalyse repo: %s\nfixing commit: %s" % (remote_link, fixing_commit))
vcc = identify.git_identify(local_link, fixing_commit)
print("3.(e) VCC: %s" % vcc)
compare.git_compare(local_link, fixing_commit, vcc)
# test_blame.git_test_blame(local_link, fixing_commit)

# Case 5
remote_link = "https://github.com/apache/ignite"
local_link = "../ignite"
if not os.path.isdir(local_link):
    Repo.clone_from(remote_link, local_link, progress=Progress())
fixing_commit = "340569b8f4e14a4cb61a9407ed2d9aa4a20bdf49"
print("\nAnalyse repo: %s\nfixing commit: %s" % (remote_link, fixing_commit))
vcc = identify.git_identify(local_link, fixing_commit)
print("3.(e) VCC: %s" % vcc)
compare.git_compare(local_link, fixing_commit, vcc)
# test_blame.git_test_blame(local_link, fixing_commit)

# Case 6
remote_link = "https://github.com/apache/cxf"
local_link = "../cxf"
if not os.path.isdir(local_link):
    Repo.clone_from(remote_link, local_link, progress=Progress())
fixing_commit = "8f4799b5bc5ed0fe62d6e018c45d960e3652373e"
print("\nAnalyse repo: %s\nfixing commit: %s" % (remote_link, fixing_commit))
vcc = identify.git_identify(local_link, fixing_commit)
print("3.(e) VCC: %s" % vcc)
compare.git_compare(local_link, fixing_commit, vcc)
# test_blame.git_test_blame(local_link, fixing_commit)