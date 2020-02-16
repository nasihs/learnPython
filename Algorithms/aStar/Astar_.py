#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://github.com/isyiming/Astar-search-algorithm/blob/master/A*.py
"""
Created on Mon Dec 18 12:38:58 2017
@author: ming
"""

import cv2
import numpy as np
from skimage import io

if __name__ == "__main__":

    maps = cv2.imread("maps.png", cv2.IMREAD_GRAYSCALE)  # 读取地图图像，灰度读入。灰度为0表示障碍物
    informap = cv2.imread("maps.png")  # 用于画路径
    maps_size = np.array(maps)  # 获取图像行和列大小
    hight = maps_size.shape[0]  # 行数->y
    width = maps_size.shape[1]  # 列数->x

    star = {'位置': (50, 50), '代价': 700, '父节点': (50, 50)}  # 起点
    end = {'位置': (400, 400), '代价': 0, '父节点': (400, 400)}  # 终点

    openlist = []  # open列表，存储可能路径
    closelist = [star]  # close列表，已走过路径
    step_size = 3  # 搜索步长。
    # 步长太小，搜索速度就太慢。步长太大，可能直接跳过障碍，得到错误的路径
    # 步长大小要大于图像中最小障碍物宽度
    while 1:
        s_point = closelist[-1]['位置']  # 获取close列表最后一个点位置，S点
        add = ([0, step_size], [0, -step_size], [step_size, 0], [-step_size, 0])  # 可能运动的四个方向增量
        for i in range(len(add)):
            x = s_point[0] + add[i][0]  # 检索超出图像大小范围则跳过
            if x < 0 or x >= width:
                continue
            y = s_point[1] + add[i][1]
            if y < 0 or y >= hight:  # 检索超出图像大小范围则跳过
                continue
            G = abs(x - star['位置'][0]) + abs(y - star['位置'][1])  # 计算代价
            H = abs(x - end['位置'][0]) + abs(y - end['位置'][1])  # 计算代价
            F = G + H
            if H < 20:  # 当逐渐靠近终点时，搜索的步长变小
                step_size = 1
            addpoint = {'位置': (x, y), '代价': F, '父节点': s_point}  # 更新位置
            count = 0
            for i in openlist:
                if i['位置'] == addpoint['位置']:
                    count += 1
            for i in closelist:
                if i['位置'] == addpoint['位置']:
                    count += 1
            if count == 0:  # 新增点不在open和close列表中
                if maps[y, x] != 0:  # 非障碍物
                    openlist.append(addpoint)
        t_point = {'位置': (50, 50), '代价': 10000, '父节点': (50, 50)}
        for j in range(len(openlist)):  # 寻找代价最小点
            if openlist[j]['代价'] < t_point['代价']:
                t_point = openlist[j]
        for j in range(len(openlist)):  # 在open列表中删除t点
            if t_point == openlist[j]:
                openlist.pop(j)
                break
        closelist.append(t_point)  # 在close列表中加入t点
        # cv2.circle(informap,t_point['位置'],1,(200,0,0),-1)
        if t_point['位置'] == end['位置']:  # 找到终点！！
            print("找到终点")
            break
    # print(closelist)

    # 逆向搜索找到路径
    road = []
    road.append(closelist[-1])
    point = road[-1]
    k = 0

    while 1:
        for i in closelist:
            if i['位置'] == point['父节点']:  # 找到父节点
                point = i
                # print(point)
                road.append(point)
        if point == star:
            print("路径搜索完成")
            break

    for i in road:  # 画出规划路径
        cv2.circle(informap, i['位置'], 1, (0, 0, 200), -1)

    cv2.circle(informap, star['位置'], 5, (0, 255, 0), -1)  # 起点
    cv2.circle(informap, end['位置'], 5, (0, 255, 100), -1)  # 终点
    io.imshow(informap)
    cv2.imwrite("informap.png", informap)
