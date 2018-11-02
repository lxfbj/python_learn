#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import getopt
import traceback






class TracebackTest:
    def __init__(self, level=5):
        self.level = level

    def traceback_print_local(self):
        local_frame = sys._getframe()
        superior_frame = local_frame.f_back
        print " %d >>> %s %s %s : " % (self.level, superior_frame.f_code.co_name,
                                       superior_frame.f_code.co_filename, superior_frame.f_lineno)
    def traceback_print_all(self):
        times = 0
        local_frame = sys._getframe()
        superior_frame = local_frame.f_back
        while local_frame:
            times += 1
            print " %d <<< %s %s %s : " % (times, local_frame.f_code.co_name,
                                           local_frame.f_code.co_filename, local_frame.f_lineno)
            """
            if superior_frame:
                print " %d <<< %s %s %s : " % (times, superior_frame.f_code.co_name,
                                               superior_frame.f_code.co_filename, superior_frame.f_lineno)
            """
            local_frame = superior_frame
            superior_frame = local_frame.f_back if  local_frame else None

    def traceback_first(self):
        self.traceback_print_local()
        if self.level > 0:
            self.level -= 1
            self.traceback_second()
        else:
            self.traceback_print_all()

    def traceback_second(self):
        self.traceback_print_local()
        if self.level > 0:
            self.level -= 1
            self.traceback_first()
        else:
            self.traceback_print_all()

    def traceback_entry(self):
        self.traceback_print_local()
        self.traceback_first()


def traceback_main():
    traceback_test = TracebackTest()
    traceback_test.traceback_entry()


if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hda:p:")
        print opts, args
        debug = False
        action = "none"
        valid_actions = ("none", "traceback")
        parameters = None
        for op, value in opts:
            if op == "-h":
                print "usage --- hda:p: ---"
                print "python demo.py -h -d"
                sys.exit(0)
            elif op == "-d":
                debug = True
            elif op == "-a":
                action = value
            elif op == "-p":
                parameters = value
        if action not in valid_actions:
            raise ValueError
        if action=="traceback":
            traceback_main()
        else:
            print "demo task none."
        exit(0)
    except ValueError as value_error:
        print("parameter Error:", value_error)
        print("except Error:", sys.exc_info())
        print("traceback:" + traceback.format_exc())
        exit(-1)
