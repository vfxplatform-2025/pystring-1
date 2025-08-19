# -*- coding: utf-8 -*-
name = "pystring"
version = "1.1.3"
authors = ["Michael Taylor", "Disney"]
description = "C++ implementation of Python string methods"

build_command = "python {root}/rezbuild.py {install}"

def commands():
    env.CPATH.prepend("{root}/include")
    env.CMAKE_PREFIX_PATH.prepend("{root}")
    env.CMAKE_MODULE_PATH.prepend("{root}/lib64/cmake/pystring")
    # find_package(pystring) 직접 가리키기
    env.PYSTRING_DIR.set("{root}/lib64/cmake/pystring") 
