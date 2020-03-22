#!/usr/bin/env python

import re
import subprocess
import curses
from curses import panel
import time

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

class ElfUtil(object):
    @staticmethod
    def get_so_list(elf):
        cmd = 'ldd ' + elf
        output = subprocess.check_output(cmd, shell=True)
        ret = [ so.strip() for so in output.splitlines() ]
        return ret

class Menu(object):
    def __init__(self, items, stdscr):
        self._win = stdscr.subwin(0,0)
        self._win.keypad(True)

        self._panel = panel.new_panel(self._win)
        self._panel.hide()
        panel.update_panels()

        self._pos = 0
        self._items = items
        self._items.append(('exit','exit'))

    def display(self):
        def navigate(n):
            self._pos += n
            if self._pos < 0:
                self._pos = 0
            elif self._pos >= len(self._items):
                self._pos = len(self._items)-1

        self._panel.top()
        self._panel.show()
        self._win.clear()

        while True:
            self._win.refresh()
            curses.doupdate()
            for index, item in enumerate(self._items):
                if index == self._pos:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL

                msg = '%d. %s' % (index, item[0])
                self._win.addstr(1 + index, 1, msg, mode)

            key = self._win.getch()

            if key in [curses.KEY_ENTER, ord('\n')]:
                if self._pos == len(self._items) - 1:
                    break
                else:
                    self._items[self._pos][1]()

            elif key == curses.KEY_UP:
                navigate(-1)

            elif key == curses.KEY_DOWN:
                navigate(1)

        self._win.clear()
        self._panel.hide()
        panel.update_panels()
        curses.doupdate()

class ViewManager(object):
    def __init__(self):
        self._stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self._stdscr.keypad(True)

    def __del__(self):
        curses.nocbreak()
        self._stdscr.keypad(False)
        curses.echo()
        curses.endwin()

    def show_menu(self):
        menu_items = [
                ]
        menu = Menu(menu_items, self._stdscr)
        menu.display()

if __name__ == '__main__':
#    view = ViewManager()

    ret = ElfUtil.get_so_list('tests/hello')
    print(ret)

    #del view
