# python3.7
# encoding: utf-8
"""
@author: Chenjin.Qian
@email:  chenjin.qian@xquant.com
@file:   setup.py
@time:   2020-06-30 11:05
"""

from setuptools import setup

import get_calendar

setup(
    name="holiday_calendar",
    version=get_calendar.__version__,
    description="The holidays in China",
    author="Jingxuan",
    author_email="qian_chen_jin@163.com",
    url="https://github.com/Thchoonlophon/holiday_calendar",
    packages=["get_calendar"],
    install_requires=["pandas", "requests"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
