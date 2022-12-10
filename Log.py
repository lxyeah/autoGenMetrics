import os


class Log(object):

    def __init__(self, pro):
        self.log_file = pro + '.txt'
        if not self.check_exist():
            self.create()

    def check_exist(self):
        return os.path.exists(self.log_file)

    def create(self):
        with open(self.log_file, 'w') as f:
            f.close()

    def add(self, commit_id):
        with open(self.log_file, 'a') as f:
            f.write(commit_id + '\n')
            f.close()

    def get_finished(self):
        with open(self.log_file, 'r') as f:
            commits = f.readlines()
            f.close()
        for i in range(len(commits)):
            commits[i] = commits[i].strip()
        return commits
