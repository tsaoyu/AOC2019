from __future__ import division
from math import atan2, pi
import math
def deg_dist(pointA, pointB):
    deg = atan2(pointB[0] - pointA[0], pointB[1] - pointA[1]) * 180 / pi
    if deg < 0:
        deg = deg + 360
    dist = (pointB[1] - pointA[1]) ** 2 + (pointB[0] - pointA[0]) ** 2
    return deg, dist, pointB

def max_visibility(sitemap):
    obs = set()
    columns, rows = len(sitemap), len(sitemap[0])

    for c in range(columns):
        for r in range(rows):
            if sitemap[c][r] == "#":
                obs.add((c,r))
    max_vis = 0 
    for o_own in obs:
        vis = len({deg_dist(o_own, o_other)[0] for o_other in obs if o_own != o_other})
        if vis > max_vis:
            max_vis = vis
            result = o_own

    return max_vis, result

def vaporise_position(sitemap):
    obs = set()
   
    
    columns, rows = len(sitemap), len(sitemap[0])

    for c in range(columns):
        for r in range(rows):
            if sitemap[c][r] == "#":
                obs.add((c,r))
    
    _, result = max_visibility(sitemap)
    obs.remove(result)
    dist_list = [deg_dist(result, o_other) for o_other in obs]
    dist_sorted = sorted(dist_list, key=lambda x: (x[0], x[1]))
    pos = 1
    idx = 0 
    o_latest = dist_sorted.pop(idx)
    o_latest_angle = o_latest[0]
    while pos < 200 and dist_sorted:
        if idx >= len(dist_sorted):
            idx = 0
            o_latest_angle = None
        if o_latest_angle == dist_sorted[idx][0]:
            idx += 1
            continue
        o_latest = dist_sorted.pop(idx)
        o_latest_angle = o_latest[0]
        pos += 1
    return o_latest[2][0] * 100 +  o_latest[2][1]

if __name__ == "__main__":
    with open('input.txt','r') as f:
        output = f.read()

    sitemap = [[j for j in i] for i in output.split('\n')]
    print(max_visibility(sitemap)[0])
    print(vaporise_position(sitemap))