#!/usr/bin/env python3

# Testing if guardrailds catch these vulnerabilities

import os
import psycopg2


def shell(cmd):
    # possible command injection
    os.system(cmd)

def getSomething(query):
    # possible SQLI and data exposure
    conn = psycopg2.connect(host='localhost', database='secretdb', user='root', password='$UperP4$vv0rd')
    cur = conn.cursor()
    cur.execute(query)

    # SOMEHTING MORE

    
if __name__=='__main__':
    # TESTING
    import sys
    shell(sys.argv[1])
    getSomething(argv[100]);
