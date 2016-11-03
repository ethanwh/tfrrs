#!/usr/bin/env python

import argparse
import tfrrs

def cli():
	parser = argparse.ArgumentParser(description='Download cross country meet data from tfrrs to a series of CSV files.')
	parser.add_argument("-m","--meet",nargs=2,help="meet_name  meet_number")
	parser.add_argument("-f","--file",type=str,help="filename with a list of results to download with each line having the format (meet_name,meet_number)")
	parser.add_argument("--men",action='store_true',default=False)
	parser.add_argument("--women",action='store_true',default=False)
	parser.add_argument("--individual",action='store_true',default=False)
	parser.add_argument("--team",action='store_true',default=False)
	parser.add_argument("--all",action='store_true',default=False)

	args = parser.parse_args()
	t = tfrrs.tfrrs()
	if args.meet != None:
		if args.all:
			data = t.download_meet(args.meet[1])
			t.write_meet(data,args.meet[0])
		else:
			data = t.download_meet(args.meet[1])
			data = t.filter_meet_data(data,args.men,args.women,args.individual,args.team)
			t.write_meet(data,args.meet[0])

	if args.file != None:
		if args.all:
			t.read_input_file(args.file,True,True,True,True)
		else:
			t.read_input_file(args.file,args.men,args.women,args.individual,args.team)