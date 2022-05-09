#!/usr/bin/env python3

# Testing if guardrailds catch this posible command injection

import os


def shell(cmd):
    os.system(cmd)
