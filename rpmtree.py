#!/usr/bin/env python

import re
import subprocess

class Rpm(object):
    def __init__(self, name):
        self._name = name
        self._rpminfo = RpmUtil.get_info(self._name)

    def __str__(self):
        return self._rpminfo

    @property
    def name(self):
        return self._name

class RpmUtil(object):
    @staticmethod
    def get_all_list():
        cmd = 'rpm -qa'
        meta = subprocess.check_output(cmd, shell=True)
        rpm_list = meta.split()
        return rpm_list

    @staticmethod
    def get_info(name):
        cmd = 'rpm -qi ' + name
        data = subprocess.check_output(cmd, shell=True)
        return data

    @staticmethod
    def get_requires_list(rpm):
        except_list = [ 'ld-linux', '/sbin/ldconfig', '/usr', '.so']
        cmd = 'rpm -qR ' + rpm.name
        data = subprocess.check_output(cmd, shell=True)
        data = data.splitlines()
        requires = [ r for r in data if not r in except_list ]
        return requires

def main():
    rpm = Rpm('glibc')
    print str(rpm)
    print RpmUtil.get_requires_list(rpm)

if __name__ == '__main__':
    main()
