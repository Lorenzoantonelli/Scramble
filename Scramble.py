#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

def scramble(lenght=20):
    moves=["FB","UD","LR"]
    special=["","'","2"]
    out=""
    count=0
    last=""
    while count<lenght:
        pz=random.choice(moves)
        if pz != last:
            out+=random.choice(pz) + random.choice(special) + " "
            count+=1
            last=pz
    return out[:-1]