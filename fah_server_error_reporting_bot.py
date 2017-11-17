# fah_server_error_reporting_bot.py
#
# Follow the F@H log.txt file like tail -f.

import time


def follow(thefile):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


if __name__ == '__main__':
    logfile = open("/home/server/server2/log.txt", "r")
    loglines = follow(logfile)
    for line in loglines:
        print line,