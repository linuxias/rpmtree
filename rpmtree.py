#!/usr/bin/env python

import re
import subprocess

class Rpm(object):
    def __init__(self, name):
        self._name = name
        self._version = None
        self._release = None
        self._arch = None
        self._install_date = None
        self._group = None
        self._license = None
        self._signature = None
        self._src_rpm = None
        self._build_date = None
        self._build_host = None
        self._relocations = None
        self._vendor = None
        self._url = None
        self._vcs = None
        self._summary = None
        self.Description = None

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
    print(RpmUtil.get_info('data-provider-master'))

if __name__ == '__main__':
    main()
