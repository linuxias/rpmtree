#!/usr/bin/env python

import re
import subprocess

class RpmUtil(object):
    @staticmethod
    def get_all_list():
        cmd = 'rpm -qa'
        meta = subprocess.check_output(cmd, shell=True)
        meta = meta.decode('utf-8')
        rpm_list = meta.split()
        return ret

def main():
    rpmlist = RpmUtil.get_all_list()

if __name__ == '__main__':
    main()
