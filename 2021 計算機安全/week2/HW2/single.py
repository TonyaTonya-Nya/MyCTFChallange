#!/bin/env python3
from collections import namedtuple
from Crypto.Util.number import inverse, bytes_to_long
import hashlib
import random
from numpy import byte

Point = namedtuple("Point", "x y")
A = Point(x=3829488417236560785272607696709023677752676859512573328792921651640651429215,
          y=7947434117984861166834877190207950006170738405923358235762824894524937052000)
B = Point(x=9587224500151531060103223864145463144550060225196219072827570145340119297428,
          y=2527809441042103520997737454058469252175392602635610992457770946515371529908)
O = 'INFINITY'
a = 9605275265879631008726467740646537125692167794341640822702313056611938432994
b = 7839838607707494463758049830515369383778931948114955676985180993569200375480
p = 9631668579539701602760432524602953084395033948174466686285759025897298205383
gx = 5664314881801362353989790109530444623032842167510027140490832957430741393367
gy = 3735011281298930501441332016708219762942193860515094934964869027614672869355


def is_on_curve(P):
    if P == O:
        return True
    else:
        return (P.y**2 - (P.x**3 + a*P.x + b)) % p == 0 and 0 <= P.x < p and 0 <= P.y < p


def point_inverse(P):
    if P == O:
        return P
    return Point(P.x, -P.y % p)


def point_addition(P, Q):
    if P == O:
        return Q
    elif Q == O:
        return P
    elif Q == point_inverse(P):
        return O
    else:
        if P == Q:
            s = (3*P.x**2 + a)*inverse(2*P.y, p) % p
        else:
            s = (Q.y - P.y) * inverse((Q.x - P.x), p) % p
    Rx = (s**2 - P.x - Q.x) % p
    Ry = (s*(P.x - Rx) - P.y) % p
    R = Point(Rx, Ry)
    assert is_on_curve(R)
    return R


def point_multiply(P, d):
    bits = bin(d)[2:]
    Q = O
    for bit in bits:
        Q = point_addition(Q, Q)
        if bit == '1':
            Q = point_addition(Q, P)
    assert is_on_curve(Q)
    return Q


p = 9631668579539701602760432524602953084395033948174466686285759025897298205383
gx = 5664314881801362353989790109530444623032842167510027140490832957430741393367
gy = 3735011281298930501441332016708219762942193860515094934964869027614672869355
G = Point(gx, gy)

d = 1532487521612462894579517163606359285989568203515734083099567402780433190052
k = point_multiply(B, d).x
print(k)
k = hashlib.sha512(str(k).encode('ascii')).digest()
FLAG = bytes.fromhex(
    '1536c5b019bd24ddf9fc50de28828f727190ff121b709a6c63c4f823ec31780ad30d219f07a8c419c7afcdce900b6e89b37b18b6daede22e5445eb98f3ca2e40')
enc = bytes(ci ^ ki for ci, ki in zip(FLAG.ljust(len(k), b'\0'), k))
print('enc =', enc)

# FLAG{adbffefdb46a99fad0042dd3c10fdc414fadd25c}
