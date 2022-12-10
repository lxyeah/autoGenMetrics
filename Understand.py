import os.path
import configure as cnf
import cmd_tool as cmd


class Understand(object):

    def __init__(self, udb_file):
        self.udb_file = udb_file

    def create(self,  pro_path, languages='java'):
        command = 'und create -languages {} add {} analyze -all {}'.format(languages, pro_path, self.udb_file)
        print(command)
        cmd.execute(command)

    def setting(self, category, option, value):
        command = 'und settings -{}{} {} {}'.format(category, option, value, self.udb_file)
        print(command)
        cmd.execute(command)

    def metrics(self):
        command = 'und metrics {}'.format(self.udb_file)
        print(command)
        cmd.execute(command)
