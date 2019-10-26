# Created by Wuli.Zuo a1785343
# 26/Oct/2019

from git import Repo

# Function of git commands to compare two commits
def git_compare(local_link, fixing_commit, vcc):
    # Create repo object
    repo = Repo(local_link)

    # VCC:
    # Affected files
    files_vcc = repo.git.show('--name-only', '--format=', vcc).splitlines()
    print("Affected files in VCC: %d" % len(files_vcc))
    # for file in files_vcc:
    #     print("     %s" % (file))

    # Fixing commit:
    # Affected files
    files_fix = repo.git.show('--name-only', '--format=', fixing_commit).splitlines()
    print("Affected files in fixing commit: %d" % len(files_fix))
    # for file in files_fix:
    #     print("     %s" % (file))

    # Find the fixed files
    files_target = list(set(files_vcc).intersection(set(files_fix)))
    if len(files_target) == 0:
        print("No common files found.")
    else:
        print("Fixed file: %d" % len(files_target))
        for file in files_target:
            print("     %s" % (file))

        # Number of days between two commit
        print("Number of days between vcc and fixing commit")
        total_days = 0
        for file in files_target:
            vcc_time = repo.git.log(-1, '--format=%ct', vcc, file).splitlines()[0]
            fixing_time = repo.git.log(-1, '--format=%ct', fixing_commit, file).splitlines()[0]
            # convert unit from seconds to days
            days = (float(fixing_time) - float(vcc_time)) / (60 * 60 * 24)
            total_days += days
            print("     %s: %.2f" % (file, days))
        avg_days = total_days / len(files_target)
        print("     The average number of days between two commits: %.2f" % avg_days)

        # Is the same developer?
        print("Developers who have modified each file: ")
        total_authors = 0
        for file in files_target:
            vcc_authors = repo.git.log(-1, '--follow', '--format=%aN', vcc, file).splitlines()
            vcc_authors.sort()
            fixing_authors = repo.git.log(-1, '--follow', '--format=%aN', fixing_commit, file).splitlines()
            fixing_authors.sort()
            print("     file: %s " % file)
            print("          Developers of VCC: %s " % vcc_authors)
            print("          Developers of fixing_commit: %s " % fixing_authors)
            target_authors = list(set(vcc_authors).intersection(set(fixing_authors)))
            if len(target_authors) == 0:
                print("     Different developers.")
            else:
                print("     Same developer(s).")