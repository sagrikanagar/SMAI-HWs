import csv
import math
name = []
age = []
height = []
role = []
bat = []
bowl = []
odi = []

f = open('Ass1.csv', 'r')
csvreader = csv.reader(f)
c = 0
for rows in csvreader:
    name.append(rows[0])
    age.append(int(rows[1]))
    height.append(float(rows[2]))
    role.append(int(rows[3]))
    bat.append(float(rows[4]))
    bowl.append(float(rows[5]))
    odi.append(int(rows[6]))

def coeff1(a):
    return 1;

def coeff(a):
    s = 0
    mu = 0
    for i in a:
        s = s + (i * i)
        mu = mu + i
    s = s / len(a)
    mu = mu / len(a)
    return 1.0 / (s - (mu * mu))


def most_similar(s):
    # who is most similar to s in Indian Team?
    idx = -1
    for i in range(len(name)):
        if name[i] == s:
            idx = i
            break
    dist = 100000000000000000000000000000000000
    ldist= 100000000000000000000000000000000000
    lpos = -1
    pos = -1
    print(coeff(age), coeff(bat));
    for i in range(15):
        l = (age[i] - age[idx]) * (age[i] - age[idx]) + (height[i] - height[idx]) * (height[i] - height[idx]) + (role[i] - role[idx]) * (role[i] - role[idx]) + (bat[i] - bat[idx]) * (bat[i] - bat[idx]) + (bowl[i] - bowl[idx]) * (bowl[i] - bowl[idx]) + (odi[i] - odi[idx]) * (odi[i] - odi[idx])
        d = coeff(age) * (age[i] - age[idx]) * (age[i] - age[idx]) + coeff(height) * (height[i] - height[idx]) * (height[i] - height[idx]) + coeff(role) * (role[i] - role[idx]) * (role[i] - role[idx]) + coeff(bat) * (bat[i] - bat[idx]) * (bat[i] - bat[idx]) + coeff(bowl) * (bowl[i] - bowl[idx]) * (bowl[i] - bowl[idx]) + coeff(odi) * (odi[i] - odi[idx]) * (odi[i] - odi[idx])
        
        l = math.sqrt(l)
        d = math.sqrt(d)
        print("Similarity of %s with %s = %f" % (name[i], name[idx], l))
        print("Weighted Similarity of %s with %s = %f" % (name[i], name[idx], d))
        if l < ldist:
            ldist = l
            lpos = i
        if d < dist:
            dist = d
            pos = i
    print(name[lpos])
    print(name[pos])

most_similar('Kumar Sangakkara')
most_similar('David Warner')
most_similar('Steve Smith')
