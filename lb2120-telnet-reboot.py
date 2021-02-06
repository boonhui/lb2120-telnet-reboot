#!/usr/bin/env python3
#
# Reboot Netgear LB2120 device via telnet interface
#
# Usage: lb2120-telnet-reboot.py <device ip or name>
#

import os
import re
import sys
import telnetlib


def exit_with_usage():

    print("Usage: lb2120-telnet-reboot.py <device ip or name>")
    os._exit(1)


def main():

    if len(sys.argv) != 2:
        exit_with_usage()

    valid_ip_pattern = r"""
        ^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}
        ([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25\[0-5])$"""
    is_valid_ip = re.match(valid_ip_pattern, sys.argv[1], re.VERBOSE)

    valid_hostname_pattern = r"""
        ^(([a-zA-Z]|[a-zA-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*
        ([A-Za-z]|[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9])$"""
    is_valid_hostname = re.match(valid_hostname_pattern, sys.argv[1],
                                 re.VERBOSE)

    if is_valid_ip is None and is_valid_hostname is None:
        exit_with_usage()

    device_addr = sys.argv[1]

    try:
        client = telnetlib.Telnet(device_addr, 5510, 10)
        client.write(b"AT+CFUN=1,1\n")
        client.read_until(b"OK", 10)

    except Exception:
        print("ERROR: can't open telnet connection to %s." % device_addr)

    finally:
        try:
            client.close()
        except Exception:
            pass


if __name__ == '__main__':
    main()
