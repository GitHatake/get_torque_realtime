#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from sympy import *

# ang1~ang7を変数として定義
ang1 = Symbol("ang1")
ang2 = Symbol("ang2")
ang3 = Symbol("ang3")
ang4 = Symbol("ang4")
ang5 = Symbol("ang5")
ang6 = Symbol("ang6")
ang7 = Symbol("ang7")


T1 = np.matrix([
    [cos(ang1), -sin(ang1), 0, 0],
    [sin(ang1), cos(ang1), 0, 0],
    [0, 0, 1, 215],
    [0, 0, 0, 1]
])

T2 = np.matrix([
    [cos(ang2), -sin(ang2), 0, 0],
    [0, 0, 1, 0],
    [-sin(ang2), -cos(ang2), 0, 0],
    [0, 0, 0, 1]
])

T3 = np.matrix([
    [cos(ang3), -sin(ang3), 0, 0],
    [0, 0, -1, -300],
    [sin(ang3), cos(ang3), 0, 0],
    [0, 0, 0, 1]
])

T4 = np.matrix([
    [cos(ang4), -sin(ang4), 0, 0],
    [0, 0, 1, 0],
    [-sin(ang4), -cos(ang4), 0, 0],
    [0, 0, 0, 1]
])

T5 = np.matrix([
    [cos(ang5), -sin(ang5), 0, 0],
    [0, 0, -1, -300],
    [sin(ang5), cos(ang5), 0, 0],
    [0, 0, 0, 1]
])

T6 = np.matrix([
    [cos(ang6), -sin(ang6), 0, 0],
    [0, 0, 1, 0],
    [-sin(ang6), -cos(ang6), 0, 0],
    [0, 0, 0, 1]
])

T7 = np.matrix([
    [cos(ang7), -sin(ang7), 0, 0],
    [0, 0, -1, -170],
    [sin(ang7), cos(ang7), 0, 0],
    [0, 0, 0, 1]
])

T8 = np.matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 150],
    [0, 0, 0, 1]
])

T_all = T1 * T2 * T3 * T4 * T5 * T6 * T7 * T8

#print(T_all)

# 各要素を変数に代入
R11, R12, R13, R14 = T_all[0, :4].tolist()[0]
R21, R22, R23, R24 = T_all[1, :4].tolist()[0]
R31, R32, R33, R34 = T_all[2, :4].tolist()[0]
R41, R42, R43, R44 = T_all[3, :4].tolist()[0]


# Roll, Pitch, Yawを計算
R = atan2(R23, R13)
P = atan2(sqrt(R13**2 + R23**2), R33)
Y = atan2(R32, -R31)


#ヤコビ行列Jrを計算
Jr11 = diff(R14, ang1)
Jr12 = diff(R14, ang2)
Jr13 = diff(R14, ang3)
Jr14 = diff(R14, ang4)
Jr15 = diff(R14, ang5)
Jr16 = diff(R14, ang6)
Jr17 = diff(R14, ang7)

Jr21 = diff(R24, ang1)
Jr22 = diff(R24, ang2)
Jr23 = diff(R24, ang3)
Jr24 = diff(R24, ang4)
Jr25 = diff(R24, ang5)
Jr26 = diff(R24, ang6)
Jr27 = diff(R24, ang7)

Jr31 = diff(R34, ang1)
Jr32 = diff(R34, ang2)
Jr33 = diff(R34, ang3)
Jr34 = diff(R34, ang4)
Jr35 = diff(R34, ang5)
Jr36 = diff(R34, ang6)
Jr37 = diff(R34, ang7)

Jr41 = diff(R, ang1)
Jr42 = diff(R, ang2)
Jr43 = diff(R, ang3)
Jr44 = diff(R, ang4)
Jr45 = diff(R, ang5)
Jr46 = diff(R, ang6)
Jr47 = diff(R, ang7)

Jr51 = diff(P, ang1)
Jr52 = diff(P, ang2)
Jr53 = diff(P, ang3)
Jr54 = diff(P, ang4)
Jr55 = diff(P, ang5)
Jr56 = diff(P, ang6)
Jr57 = diff(P, ang7)

Jr61 = diff(Y, ang1)
Jr62 = diff(Y, ang2)
Jr63 = diff(Y, ang3)
Jr64 = diff(Y, ang4)
Jr65 = diff(Y, ang5)
Jr66 = diff(Y, ang6)
Jr67 = diff(Y, ang7)

Jr = np.matrix((
    [Jr11, Jr12, Jr13, Jr14, Jr15, Jr16, Jr17],
    [Jr21, Jr22, Jr23, Jr24, Jr25, Jr26, Jr27],
    [Jr31, Jr32, Jr33, Jr34, Jr35, Jr36, Jr37],
    [Jr41, Jr42, Jr43, Jr44, Jr45, Jr46, Jr47],
    [Jr51, Jr52, Jr53, Jr54, Jr55, Jr56, Jr57],
    [Jr61, Jr62, Jr63, Jr64, Jr65, Jr66, Jr67]
))


#ヤコビ行列Jvを計算
H = np.matrix((
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, -sin(R), -cos(R)*sin(P)],
    [0, 0, 0, 0, cos(R), sin(R)*sin(P)],
    [0, 0, 0, 1, 0, cos(P)]
))

Jv = H * Jr

print(Jv)

# 行列の各要素を文字列に変換
Jv_str = Jv.__str__()

# テキストファイルに書き込む
with open('jacobiandata_text.txt', 'w') as file:
    file.write(Jv_str)