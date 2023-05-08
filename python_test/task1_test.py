import pytest
import subprocess
import os
from pathlib import Path



def test_task1():
    path2 = Path(__file__).parent.absolute()
    print (path2)
    comlist = [f'{path2}/task1.py']
    script = b'1\n2\n\n'
    res = subprocess.run(comlist, input=script,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print (res)
    # assert res.returncode == 0
    assert res.stdout==b'2.0\n'
    #assert res.stderr

def test_task2():
    path2 = Path(__file__).parent.absolute()
    print (path2)
    comlist = [f'{path2}/task2.py']
    script = b'1\n2\n\n'
    res = subprocess.run(comlist, input=script,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print (res)
    # assert res.returncode == 0
    assert res.stdout==b'2.0\n'
#
# scripts = pathlib.Path(__file__, '..', 'scripts').resolve().glob('*.py')
#
#
# @pytest.mark.parametrize('script', scripts)
# def test_script_execution():
#     runpy.run_module("task1.py")


#
# def test_myoutput(capsys):  # or use "capfd" for fd-level
#     print("hello")
#     sys.stderr.write("world\n")
#     captured = capsys.readouterr()
#     assert captured.out == "hello\n"
#     assert captured.err == "world\n"
#     print("next")
#     captured = capsys.readouterr()
#     assert captured.out == "next\n"
