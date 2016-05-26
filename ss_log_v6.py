import operator

# Open the log file
f=open('d:\shadowsocks.log')

# dic to store the ip
s={}

# begin to read log
for line in f:

	# find ip address start location,ipv6 address begin with '::ffff:'
	loc = line.find('::ffff:');
	if  loc != -1:

		# if find ip,then find the ':' before the port number,find from the loc+8
		loc_p = line.find(':',loc+8)

		# cut out ip form the line
		ip = line[loc+7:loc_p]

		# if ip not in the dic
		if ip not in s:
			# add ip to the set
			s.update({ip:1})
		# if ip in the dic
		else:
			s[ip]+=1

for w in sorted(s, key=s.get, reverse=True):
  # Uncomment to print ips with its connected times
  print(w+'		'+str(s[w]))

  # Just print ips
  #print(w)

f.close()
