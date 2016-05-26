# Open the log file
f=open('shadowsocks.log')

# initial a blank set
s={1}
s.remove(1)

# begin to read log
for line in f:

	# find ip address start location,ip v4 address begin with '::ffff:'
	loc = line.find('::ffff:');
	if  loc != -1:

		# if find ip,then find the ':' before the port number,find from the loc+8
		loc_p = line.find(':',loc+8)

		# cut out ip form the line
		ip = line[loc+7:loc_p]

		# if ip not in the set
		if ip not in s:
			print(ip)

			# add ip to the set
			s.add(ip)
f.close()
