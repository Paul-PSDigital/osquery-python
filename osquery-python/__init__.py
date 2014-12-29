import subprocess

''' Python Module for OSQuery

TODO: use SWIG to bind to Cpp osquery code
'''
class osquery:
    outputMode = "--json" 
    ''' Set the output mode to use

    Known supported options: csv, json, html, line, list
    '''
    def setOutputMode(self, mode):
       self.outputMode = mode
       return self
    
    ''' Perform an osquery

    Returns the result of the osquery 
    '''
    def query(self, cmd):
       p1 = subprocess.Popen(["echo", cmd, ";"], stdout=subprocess.PIPE)
       p2 = subprocess.Popen(["osqueryi", self.outputMode], stdin=p1.stdout, stdout=subprocess.PIPE)
       p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
       output,err = p2.communicate()
       return output

osquery = osquery()
osquery.setOutputMode("--json").query("SELECT * from etc_hosts")
