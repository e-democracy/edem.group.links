# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

#-----------------------------------------------------------------------------#

version = '2.0.0'
release = False

#-----------------------------------------------------------------------------#

import sys
if (sys.version_info < (3, )):
    from commands import getstatusoutput
else:
    from subprocess import getstatusoutput  # lint:ok
import datetime
import os
import glob

class CommandError(Exception):
    pass


def execute_command(commandstring):
    status, output = getstatusoutput(commandstring)
    if status != 0:
        raise CommandError
    return output


def parse_version_from_package():
    try:
        pkginfo = os.path.join(glob.glob('*.egg-info')[0], 'PKG-INFO')
    except:
        pkginfo = ''

    version_string = ''
    if os.path.exists(pkginfo):
        for line in open(pkginfo):
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

        if release:
            version_string = version
        else:
            version_string = "%s.dev%s-%s" % (version, datestring, commithash)

    except CommandError:
        version_string = parse_version_from_package()

    return version_string


if __name__ == '__main__':
    print get_version()
    sys.stdout.write('{0}\n'.format(get_version()))
