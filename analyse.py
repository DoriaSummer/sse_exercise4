# Created by Wuli.Zuo a1785343
# 9/Sep/2019

from git import Repo
import re

# Function of git commands to analyse commits

def git_analyse(local_link, fixing_commit):

    # Create repo object
    repo = Repo(local_link)

    # Reset to given commit
    output_0 = repo.git.reset('--hard', fixing_commit)
    print("Current fix commit:\n%s" % output_0)
      
    # Question a: get commit message and title
    output_a = repo.git.log(-1, '--format=%B')
    print("\n(a). Commit message and title:\n%s" % output_a)

    # Question b: get number of affected files
    output_b = repo.git.show('--name-only', '--format=').splitlines()
    print("(b). Number of affected files: %d" % len(output_b))
    
    # Question c: get number of affected directories
    output_c = repo.git.show('--dirstat', '--format=').splitlines()
    print("(c). Number of affected directories: %d" % len(output_c))
    
    # Question d: get number of deleted lines (including comments and blank lines)
    lines = repo.git.show().splitlines()
    # Lines start with '-', but not followed by '-', can be followed arbitrary number of blanks
    output_d = [line for line in lines if re.compile('^-[^-]|^-\s*$').match(line)]
    print("(d). Number of deleted lines (including comments and blank lines): %d" % len(output_d))

    # Question e: get number of added lines (including comments and blank lines)
    lines = repo.git.show().splitlines()
    # Lines start with '+', but not followed by '+', can be followed arbitrary number of blanks
    output_e = [line for line in lines if re.compile('^\+[^\+]|^\+\s*$').match(line)]
    print("(e). Number of added lines (including comments and blank lines): %d" % len(output_e))

    # Question f: get number of deleted lines (excluding comments and blank lines)
    lines = repo.git.show().splitlines()
    # lines start with '-', but not followed by '-'; excluding /*, *, */, // and blank lines
    lines = [line for line in lines if re.compile('^-[^-]|^-\s*$').match(line)]
    lines = [line for line in lines if not re.compile('^-\s*\/').match(line)]
    lines = [line for line in lines if not re.compile('^-\s*\*').match(line)]
    output_f = [line for line in lines if not re.compile('^-\s*$').match(line)]
    print("(f). Number of deleted lines (including comments and blank lines): %d" % len(output_f))

    # Question g: get number of added lines (excluding comments and blank lines)
    lines = repo.git.show().splitlines()
    # lines start with '+', but not followed by '+'; excluding /*, *, */, // and blank lines
    lines = [line for line in lines if re.compile('^\+[^\+]|^\+\s*$').match(line)]
    lines = [line for line in lines if not re.compile('^\+\s*\/').match(line)]
    lines = [line for line in lines if not re.compile('^\+\s*\*').match(line)]
    output_g = [line for line in lines if not re.compile('^\+\s*$').match(line)]
    print("(g). Number of added lines (including comments and blank lines): %d" % len(output_g))

    # Question h: number of days between two commit
    print("(h). Number of days between the current fixing commit and the previous commit: ")
    total_days = 0
    for file in repo.git.show('--name-only', '--format=').splitlines():
        # Check if a file is a new added file in current commit
        output_h = repo.git.log(-2, '--format=%ct', file).splitlines()
        if(len(output_h) == 1):
            print("     %s: new added file  0" % file)
        else:
            # convert unit from seconds to days
            days = (float(output_h[0])-float(output_h[1]))/(60*60*24)
            total_days += days
            print("     %s: %.2f" % (file, days))
    avg_days = total_days / len(output_b)
    print("     The average number of days between two commits: %.2f" % avg_days)

    # Question i: number of times each affected file has been modified
    print("(i). Number of times each file has been modified: ")
    total_times = 0
    for file in repo.git.show('--name-only', '--format=').splitlines():
        output_i = repo.git.log('--follow', '--format=oneline', file).splitlines()
        total_times += len(output_i)
        print("     %s:  %d" % (file, len(output_i)))
    avg_times = total_times / len(output_b)
    print("     The average number of modified times: %.2f" % avg_times)

    # Question j: developers who have modified each file
    print("(j). Developers who have modified each file: ")
    total_authors = 0
    for file in repo.git.show('--name-only', '--format=').splitlines():
        print("     Developers who have modified file: %s " % file)
        authors = repo.git.log('--follow', '--format=%aN', file).splitlines()
        for author in set(authors):
            print("       %s"%author)
            total_authors = total_authors + 1
    avg_authors = total_authors / len(output_b)
    print("     The average number of developers modified each file: %.2f" % avg_authors)

    # Question k: number of commits each developer has made
    print("(k). Number of commits each developer has made: ")
    authors = set()
    for file in repo.git.show('--name-only', '--format=').splitlines():
        authors.update(repo.git.log('--format=%aN', file).splitlines())
    authors = list(authors)
    authors.sort()
    for author in authors:
        commits_time = len(re.findall(author,repo.git.log('--format=%aN')))
        if commits_time >= 100:
            print("     %s: %d  This is an experienced developer." % (author, commits_time))
        else:
            print("     %s: %d  This is an new developer." % (author, commits_time))
    print("     Total number of developers modified the affected files: %d" % len(authors))