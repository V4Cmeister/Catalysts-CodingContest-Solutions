import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 7000))
sw = s.makefile(mode="w")
sr = s.makefile(mode="r")

def readData():
	playerData = sr.readline().strip().split()
	playerData = [float(playerData[1]),float(playerData[2])]
	cpuData = sr.readline().strip().split()
	cpuData = [float(cpuData[1]),float(cpuData[2])]
	ballData = sr.readline().strip().split()
	ballData = [float(x) for x in ballData[1:]]
	return playerData, cpuData, ballData

def computeMove(player,cpu,ball):
	ballr = 15
	xLine = (25+ballr-ball[0]) if ball[2]<0 else (1500-ballr-ball[0])
	to = ball[1]+ball[3]*xLine/ball[2]
	while to<0 or to>600:
		if to<0:
			to*=-1
		if to>=600:
			to = 1200-to	
	return max(-36,min(36,int(to-(player[0]+player[1]+75))))


while(True):
	player,cpu,ball = readData()
	sr.readline()
	move = computeMove(player,cpu,ball)
	sw.write('move '+str(move)+'\n')
	sw.flush()
