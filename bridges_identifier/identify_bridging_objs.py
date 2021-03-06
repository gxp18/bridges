def identify():

	# Dictionary Construction to map read-to-write
	ops_map = {}
	ops_map["read"] = ["write", "append", "override"]
	ops_map["getattr"] = ["setattr"]
	ops_map["relabelfrom"] = ["relabelto"]
	ops_map["execute"] = ["write", "append"]
	ops_map["recvfrom"] = ["sendto"]
	ops_map["recv_msg"] = ["send_msg"]
	ops_map["unix_read"] = ["unix_write"]
	ops_map["getfocus"] = ["setfocus"]
	ops_map["list_property"] = ["set_property"]
	ops_map["get_property"] = ["set_property"]
	ops_map["quotaget"] = ["quotamod"]
	ops_map["tcp_recv"] = ["tcp_send"]
	ops_map["udp_recv"] = ["udp_send"]
	ops_map["rawip_recv"] = ["rawip_send"]
	ops_map["dccp_recv"] = ["dccp_send"]
	ops_map["ingress"] = ["egress"]
	ops_map["acceptfrom"] = ["connectto"]
	ops_map["getsched"] = ["setsched"]
	ops_map["getpgid"] = ["setpgid"]
	ops_map["getcap"] = ["setcap"]
	ops_map["receive"] = ["send"]
	ops_map["dac_read_search"] = ["dac_override"]
	ops_map["nlmsg_read"] = ["nlmsg_write"]
	ops_map["recv"] = ["send"]
	ops_map["flow_in"] = ["flow_out"]
	ops_map["forward_in"] = ["forward_out"]
	ops_map["select"] = ["update", "insert", "delete"]
	ops_map["execute"] = ["install"]
	ops_map["import"] = ["export"]
	ops_map["search"] = ["add_name", "remove_name"]
	ops_map["get_value"] = ["set_value"]
	ops_map["find"] = ["add"]
	ops_map["list"] = ["add"]
	ops_map["get"] = ["insert", "delete"]
	ops_map["list"] = ["insert", "delete"]
	ops_map["verify"] = ["sign"]
	ops_map["getopt"] = ["setopt"]
	ops_map["manage"] = ["manage"]
	ops_map["open"] = ["open"]
	ops_map["execmod"] = ["open"]


	# STEP 1 - Get Read Objects 
	obj_read = open("./out/read_objects.out", 'w')
	stage = 0
	skip = 0
	count = 0

	with open('./out/read_allows.out') as f:
		for line in f:
			for c in line:
				if c == ' ' and stage == 0:
					stage = 1
					continue
				elif c == ' ' and stage == 1 and skip == 0:
					stage = 2
					continue
				elif stage == 4:
					obj_read.write(" ") #new
					break						
				elif c == ':' and stage == 2:
					stage = 3
					obj_read.write(c)
					continue
				elif c == '{' and stage == 1 and skip == 0:
					skip = 1
				elif c == '}' and stage == 1 and skip == 1:
					skip = 0
				elif stage == 2:
					obj_read.write(c)
				elif c == '{' and stage == 3 and skip == 0:
					skip = 1
					obj_read.write(c)
				elif c == '}' and stage == 3 and skip == 1:
					skip = 0
					obj_read.write(c)

				elif c == ' ' and stage == 3 and skip == 0:
					stage = 4
					continue

				elif c == ' ' and stage == 3 and skip == 1:
					obj_read.write(c)
					continue
				elif stage == 3:
					obj_read.write(c)				
			obj_read.write('\n')
			skip = 0
			stage = 0	
	f.close()
	obj_read.close()

	# STEP 2 - Get Target Object of untrusted
	obj_written = open("./out/written_objects.out", 'w')
	stage = 0
	skip = 0
	with open('./out/write_allows.out') as f:
		for line in f:
			for c in line:
				if c == ' ' and stage == 0:
					stage = 1
					continue
				elif c == ' ' and stage == 1 and skip == 0:
					stage = 2
					continue
				elif c == ' ' and stage == 3 and skip == 0:
					stage = 4
					continue

				elif c == ' ' and stage == 3 and skip == 1:
					obj_written.write(c)
					continue
				elif stage == 4:
					obj_written.write(" ") #new
					break						
				elif c == ':' and stage == 2:
					stage = 3
					obj_written.write(c)
					continue
				elif c == '{' and stage == 1 and skip == 0:
					skip = 1
				elif c == '}' and stage == 1 and skip == 1:
					skip = 0
				elif stage == 2:
					obj_written.write(c)
				elif c == '{' and stage == 3 and skip == 0:
					skip = 1
					obj_written.write(c)
				elif c == '}' and stage == 3 and skip == 1:
					skip = 0
					obj_written.write(c)
				elif stage == 3:
					obj_written.write(c)
			obj_written.write('\n')
			skip = 0
			stage = 0
	f.close()
	obj_written.close()

	# STEP 3 - Identify Conflicting Objects
	conflicts = open('./out/bridging_objects.out', 'w')
	with open('./out/written_objects.out', 'r') as file1:
	    with open('./out/read_objects.out', 'r') as file2:
		same = set(file1).intersection(file2)
	same.discard('\n')

	for obj in same:
		conflicts.write(obj)
		conflicts.write("\tWRITES: \n")
		with open('./out/write_allows.out') as f2:
			for line2 in f2:
				if (" "+obj.rstrip('\n')) in line2:
					conflicts.write('\t\t' + line2)
		conflicts.write("\tREADS: \n")
		with open('./out/read_allows.out') as f1:
			for line1 in f1:
				if (" "+ obj.rstrip('\n')) in line1:
					conflicts.write('\t\t' + line1)

	# STEP 4 - Retrieve Neverallows for Conflicting Objects
		conflicts.write("\tNEVERALLOWS: \n")
		count = count + 1
		with open('./out/neverallows.out') as f3:
			for line3 in f3:
				if obj.rstrip('\n') in line3:
					conflicts.write('\t\t' + line3)
		conflicts.write('\n')
	conflicts.write("Bridging Objects = " + str(count)+"\n");
	f1.close()
	f2.close()
	conflicts.close()


if __name__ == '__main__':
    indentify()
