#!/usr/bin/env python

import os
import datetime
import signal
import time
import subprocess


class CmdTimeoutError(Exception):
    pass

def exec_cmd(command, timeout=None, stdout=None, stderr=None, stdin=None):
    """
    Set timeout=None to run without timeout
    
    To capture stdout, set them to subprocess.PIPE, and then access it 
    from process.stdout.read()
    e.g. process = exec_cmd(command, stdout=subprocess.PIPE)
    
    To capture both stdout and stderr:
    e.g. process = exec_cmd(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    process.returncode  
    process.stdout.read() : process.stdout is None if empty
    process.stderr.read()
    """
    #shell command with timeout
    start = datetime.datetime.now()
    process = subprocess.Popen(command, shell=True, stdout=stdout, stderr=stderr)
    while process.poll() is None: 
        time.sleep(0.1)
        now = datetime.datetime.now()
        if timeout is not None and (now - start).seconds > timeout:
            os.kill(process.pid, signal.SIGKILL)
            os.waitpid(-1, os.WNOHANG)
            pipeout = '\n' . join([s.read() for s in [process.stdout, process.stderr] if s is not None])
            raise CmdTimeoutError('Command timeout: %s\n%s' % (command, pipeout))

    return process


