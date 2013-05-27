

Installation
------------

``pip install exec_cmd``

Usage
-----

Set ``timeout=None`` to run without timeout. For timeout::

    exec_cmd("ls", timeout=30)

To capture stdout, set them to ``subprocess.PIPE``, and then access it::

    from process.stdout.read()
    process = exec_cmd(command, stdout=subprocess.PIPE)

To capture both stdout and stderr::

    process = exec_cmd(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    process.returncode
    process.stdout.read() : process.stdout is None if empty
    process.stderr.read()


