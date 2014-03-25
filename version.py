version='2.00'
release=False

#-------------------------------------------------------------------------------------#

import commands
import datetime
import os
import glob

class CommandError(Exception):
    pass

def execute_command(commandstring):
    status, output = commands.getstatusoutput(commandstring)
    if status != 0:
        raise CommandError
    return output

def parse_version_from_package():
    try:
        pkginfo = os.path.join(glob.glob('*.egg-info')[0],
                                         'PKG-INFO')
    except:
        pkginfo = ''
    
    version_string = ''
    if os.path.exists(pkginfo):
        for line in file(pkginfo):
            if line.find('Version: ') == 0:
                version_string = line.strip().split('Version: ')[1].strip()
        if not version_string:
            version_string = '%s-dev' % version
    else:
        version_string = version
    
    return version_string

def get_version():
    try:
        gitLog = execute_command('git log -1 --format="%ct-%H"')
        (commitdate, dash, commithash) = gitLog.partition('-')
        dt = datetime.datetime.utcfromtimestamp(float(commitdate))
        datestring = dt.strftime('%Y%m%d%H%M%S')

        version_string = "%s-%s-%s" % (version, datestring, commithash)

    except CommandError, IntegerError:
        version_string = parse_version_from_package()

    return version_string

if __name__ == '__main__':
    print get_version()



