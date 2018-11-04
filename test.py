#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import getopt
import traceback
from mc.license import License
from mc.version import get_mc_version
from mc.version import init_mc_version
from mc import log
LOG = log.getLogger()




def test_except_print(test_except_str):
    print "test_except_print:", test_except_str
    return test_except_str


def test_except():
    try:
        raise ValueError
        pass
    except ValueError as e:
        print("test_except_e: %s", e)
        return test_except_print("test_except_t: %s" % "1")
    finally:
        return test_except_print("test_except: %s" % "2")
    return test_except_print("test_except_t: %s" % "3")


def test_task_list():
    all_task_list = [
        {
            "valid": False,
            "task_name": ""
        }
    ]
    return all_task_list


if __name__ == "__main__":
    try:
        # noinspection PyBroadException
        opts, args = getopt.getopt(sys.argv[1:], "hda:p:")
        errcode = 0
        debug = False
        version = "debug"
        valid_versions = ("release", "test", "debug")
        action = "none"
        valid_actions = ("none", "test")
        parameters = None
        print opts, args
        for op, value in opts:
            if op == "-h":
                print "usage --- hda:p: ---"
                print "python test.py -h -d"
                sys.exit(0)
            elif op == "-d":
                debug = True
            elif op == "-a":
                action = value
            elif op == "-p":
                parameters = value
        if action not in valid_actions:
            raise ValueError
        for arg in args:
            if arg in valid_versions:
                version = arg
            else:
                raise ValueError
        if action == "test":
            file_path = None
            name = None
            user = None
            if debug:
                file_path = file_path if file_path else '/root/jl/license/lic_MC_P1_4096.lic'
                name = name if name else 'test_lic_MC_P1_4096.lic'
                user = user if user else '5b602917b30b8b7a110a016f'
                print "file_path: %s," % file_path + "name: %s," % name + "user: %s" % user
            if not version:
                version = get_mc_version()
            if not version:
                print "The main program did not start."
                exit(0)
            # test bundle license management
            init_mc_version(version)
            lic = License()
            errcode = lic.UploadBundleLicense(file_path, name, user)
            errmsg = lic.GetBundleLicenseErrMsg(errcode)
            print errmsg
        else:
            print test_except()
            pass
        exit(0)
    except ValueError as value_error:
        print("parameter Error:", value_error)
        print("except Error:", sys.exc_info())
        print("traceback:" + traceback.format_exc())
        exit(-1)
