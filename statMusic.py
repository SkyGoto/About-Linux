#!/usr/bin/env python3.6

import os
import sys
import argparse
import threading
import time


class NeteaseCloudMusic(threading.Thread):
    def run(self):
        if self.commend:
            self.start_music()
        else:
            time.sleep(1)

    def __init__(self , commend):
        super(NeteaseCloudMusic, self).__init__()
        self.music_status = self.get_pid()
        self.commend = commend

    def get_pid(self):
        return os.popen('ps -ef | grep "netease-cloud-music" | grep -v grep | awk \'{print $2}\' ').read()

    def start_music(self):
        '''
        if self.music_status:
            pids = self.split_pid(self.music_status)
            self.kill_pid(pids)
        '''
        os.system(self.commend)

    def split_pid(self, pids):
        return pids.split('\n')[:-1]

    def kill_pid(self, pids):
        for pid in pids:
            os.system("kill -15 "+pid)

    def set_thread(self, thread_):
        thread_.setDaemon(True)


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("-stop",dest = 'stop' ,
                       help='stop the soft',
                       action='store_const',
                       const='stop')
    args = parse.parse_args()
    if args.stop:
        tpids = os.popen('ps -ef | grep "netease-cloud-music" | grep -v grep | awk \'{print $2}\' ').read()
        tpids = tpids.split('\n')[:-1]
        for pid in tpids:
            os.system("kill -9 "+pid)
        time.sleep(0.2)
    if os.popen('ps -ef | grep "netease-cloud-music" | grep -v grep | awk \'{print $2}\' ').read():
        os.system("netease-cloud-music %U")
    else:
        thread = NeteaseCloudMusic("netease-cloud-music")
        tmp_thread = NeteaseCloudMusic("")
        music_thread = NeteaseCloudMusic("netease-cloud-music %U")
        tmp_thread.set_thread(thread)
        tmp_thread.set_thread(music_thread)
        thread.start()
        time.sleep(0.2)
        temp = thread.get_pid()
        music_thread.start()
        time.sleep(0.2)
        thread.kill_pid(thread.split_pid(temp))
        tmp_thread.start()


if __name__ == '__main__':
    main()

