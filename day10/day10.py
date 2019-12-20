from __future__ import division
from math import atan2

def max_visibility(sitemap):
    epsilon = 1e-8
    obs = set()
    max_visible = 0
    
    columns, rows = len(sitemap), len(sitemap[0])

    for c in range(columns):
        for r in range(rows):
            if sitemap[c][r] == "#":
                obs.add((c,r))

    for o_own in obs:
        visible = 0
        c_own, r_own = o_own
        for o_other in obs:
            c_other, r_other = o_other
            blocked = False

            if c_other != c_own:
                slope = (r_other - r_own) / (c_other - c_own)
                initial = r_other -  slope * c_other
                c_start = min(c_own, c_other)
                c_end = max(c_own, c_other)
                for c in range(c_start + 1, c_end):
                    r_possible = c * slope + initial
                    if r_possible - (r_possible // 1) < epsilon:
                        r_possible = int(r_possible)
                    if (c, r_possible) in obs:
                        blocked = True
                
            else:
                r_start = min(r_other, r_own)
                r_end = max(r_other, r_own)
                for r in range(r_start+1, r_end):
                    if (c_own, r) in obs:
                        blocked = True
          
            if not blocked:
                visible += 1

        if visible > max_visible:
            max_visible = visible
            pos = c_own, r_own

    return max_visible, pos

def vaporise_position(sitemap, laser_pos):
    epsilon = 1e-8
    obs = set()
    max_visible = 0
    
    columns, rows = len(sitemap), len(sitemap[0])

    def deg_dist(pointA, pointB):
        deg = atan2(pointB[0] - pointA[0], pointB[1] - pointA[1])
        dist = (pointB[1] - pointA[1]) ** 2 + (pointB[0] - pointA[0]) ** 2
        return deg, dist, pointB

    for c in range(columns):
        for r in range(rows):
            if sitemap[c][r] == "#":
                obs.add((c,r))

    dist_list = [deg_dist(laser_pos, o_other) for o_other in obs]
    
    print(sorted(dist_list, key=lambda x: (x[0], x[1]))[200])

if __name__ == "__main__":
    with open('input.txt','r') as f:
        output = f.read()

    sitemap = [[j for j in i] for i in output.split('\n')]
    print(max_visibility(sitemap)[0])
    vaporise_position(sitemap, max_visibility(sitemap)[1])
   