#!/usr/bin/env python

import re
import subprocess

class Rpm(object):
    def __init__(self, name):
        self._name = name
        self._rpminfo = RpmUtil.get_info(self._name)

    def __str__(self):
        return self._rpminfo


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

def main():
    rpm = Rpm('glibc')
    print str(rpm)

if __name__ == '__main__':
    main()
