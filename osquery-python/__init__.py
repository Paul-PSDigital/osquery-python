import subprocess

class OSQuery:
    def run_cmd(self, cmd):
       p1 = subprocess.Popen(["echo", cmd], stdout=subprocess.PIPE)
       p2 = subprocess.Popen(["osqueryi"], stdin=p1.stdout, stdout=subprocess.PIPE)
       p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
       output,err = p2.communicate()
       return output 
