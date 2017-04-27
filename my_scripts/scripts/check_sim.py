import os
import time
import subprocess

def check_sim(sleeptime):
	for index in range(0, 5):
		time.sleep(sleeptime)
		if os.path.isfile("logs/simulation.target.log"):
			with open ("logs/simulation.target.log", "r") as log:
				for line in log:
						if "-L altera_ver -L lpm_ver -L sgate_ver" in line:
							os.system("ps -W | awk '/vlm.exe/,NF=1' | xargs kill -f")
							return True
						elif index < 4:
							sleeptime = 15
						else:
							return False

os.chdir("../simulation/ethernet_lib/ARP_module/")
os.system("rm -rf logs/simulation.target.log")
if os.path.isdir("logs"):
	sleeptime=30
else:
	sleeptime=300
proc = subprocess.Popen(['make', 'simulation'])
print "start process"
print "simulation result: ", check_sim(sleeptime)
proc.terminate()