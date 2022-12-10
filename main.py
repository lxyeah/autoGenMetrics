import os
import cmd_tool as cmd
import configure as cnf
import GitRepository as git
import Understand as und
import time
import Log as log


def format_commits(path):
    with open(path, 'r') as f:
        commit_list = f.readlines()
    f.close()
    for i in range(len(commit_list)):
        commit_list[i] = commit_list[i].strip().split('.csv')[0].split('./')[1]
    return commit_list


def get_commit_list(pro, git_repo=None, from_git=False):
    if from_git:
        commit_set = git_repo.commits()
        commit_list = []
        for c in commit_set:
            commit_list.append(c['commit'])
        return commit_list
    else:
        commit_list_path = os.path.join(cnf.commit_list_dir, pro)
        return format_commits(commit_list_path)


if __name__ == '__main__':
    pro_name = 'maven-shared'

    udb_path = os.path.join(cnf.udb_dir, pro_name)
    pro_path = os.path.join(cnf.repo_dir, pro_name)
    metrics_path = os.path.join(cnf.metrics_dir, pro_name)
    remote_path = 'https://github.com/apache/maven-shared.git'

    cmd.mkdir(udb_path)

    repo = git.GitRepository(pro_path, remote_path)
    commits = get_commit_list(pro_name, repo, True)

    log_file = log.Log(pro_name)
    finished = log_file.get_finished()

    for commitId in commits:
        print('Now at ' + commitId)

        if commitId not in finished:
            repo.change_to_commit(commitId)

            udb_file = os.path.join(udb_path, pro_name + '_' + commitId + '.udb')
            metrics_file = os.path.join(metrics_path, pro_name + '_' + commitId + '.csv')

            sci_tool = und.Understand(udb_file)
            sci_tool.create(pro_path)
            sci_tool.setting('Java', 'Version', 'Java8')
            sci_tool.setting('Metric', 'Metrics', 'all')
            sci_tool.setting('Metric', 'OutputFile', metrics_file)
            sci_tool.metrics()
            time.sleep(5)

            log_file.add(commitId)

