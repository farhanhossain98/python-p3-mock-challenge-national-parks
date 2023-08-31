#!/usr/bin/env python3
import ipdb

from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    v1 = Visitor("Farhan")
    v2 = Visitor("Tanim")
    v3 = Visitor("Prithi")
    v4 = Visitor("Yeasin") 

    n1 = NationalPark('Central')
    n2 = NationalPark('Middle')
    n3 = NationalPark('Left')
    n4 = NationalPark('Right')

    t1 = Trip ( v1, n2, '8/12/23', '4/12/24')
    t2 = Trip ( v2, n3, '8/13/23', '5/12/24')
    t3 = Trip ( v4, n1, '8/4/23', '2/12/24')
    t4 = Trip ( v1, n1, '1/12/23', '3/12/24')
    t5 = Trip ( v4, n2, '5/1/23', '2/12/24')
    t6 = Trip ( v1, n2, '2/12/23', '1/12/24')

    ipdb.set_trace()
