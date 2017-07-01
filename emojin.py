# -*- coding: utf-8 -*-

import os
import sys

def file2list(filepath):
    ret = []
    with open(filepath, 'r') as f:
        ret = [line.rstrip('\n') for line in f.readlines()]
    return ret

def list2file(filepath, ls):
    with open(filepath, 'w') as f:
        f.writelines(['%s\n' % line for line in ls] )

def p(obj):
    print obj

def abort(msg):
    p('Error: {0}'.format(msg))
    exit(1)

def usage():
    msg = """[Usage]
python {0} (EmojinDataFilepath) """.format(MYFILENAME)
    p(msg)
    exit(0)

def arg2datafile():
    if len(sys.argv)<=1:
        usage()
    return sys.argv[1]

MYDIR = os.path.abspath(os.path.dirname(__file__))
MYFILENAME = os.path.basename(__file__)

infile = arg2datafile()

if not(os.path.exists(infile)):
    abort('Datafile "{0}" does not exists.'.format(infile))

# parse
# -----

lines = file2list(infile)

outlines = []
convertion_table = []
be_commented_out_mode = False

for i, line in enumerate(lines):
    # blank line.
    if len(line)==0:
        continue

    # commented out.
    if be_commented_out_mode:
        if len(line)>=2 and line[:2]=='*/':
            be_commented_out_mode = False
            continue
        # In multiple commented out.
        continue
    if len(line)>=2 and line[:2]=='//':
        continue
    if len(line)>=2 and line[:2]=='/*':
        be_commented_out_mode = True
        continue

    # inserting a blank line.
    if line=='@br':
        outlines.append('')
        continue

    # assigning to the convertion table.
    #  @a=emojiname
    #  ^ ^
    if len(line)>3 and line[0]=='@' and line[2]=='=':
        key = line[1]
        value = line[3:].replace(':', '').lower()
        convertion_table.append((key, value))
        continue

    outlines.append(line)

# convertion
# ----------

# About convertion algorithm.
#
# In case of below,
#   @-=cloud
#   @o=tomato
#   o-o-o
# If use replacing simply,
#   1 o-o-o
#   2 o:cloud:o:cloud:o
#   3 :tomato::cl:tomato:ud::tomato::cl:tomato:ud:o
# The result 3 is wrong because not ':cloud:' but ':clo:tomato:ud:'.
# So I introduced a 'special bit' to avoiding this problem.

zero = ')'
one  = '('

def int2specialbit(integer):
    # 0 )
    # 1 (
    # 2 ()
    # 3 ((
    # 4 ())
    # 5 ()(
    # 6 (()
    # 7 (((
    # ...
    bit = format(integer, 'b')
    specialbit = bit.replace('0', zero).replace('1', one)
    return specialbit

def specialbit2int(specialbit):
    bit = specialbit.replace(zero, '0').replace(one, '1')
    return int(bit, 2)

outstr = '\n'.join(outlines)

for i, kv in enumerate(convertion_table):
    key, _ = kv

    before = key
    after  = '@{0}@'.format(int2specialbit(i))

    outstr = outstr.replace(before, after)

for i, kv in enumerate(convertion_table):
    _, value = kv

    before = '@{0}@'.format(int2specialbit(i))
    after  = ':{0}:'.format(value)

    outstr = outstr.replace(before, after)

# output
# ------

p(outstr)
