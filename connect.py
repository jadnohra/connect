#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys,sqlite3,traceback

largv = []
g_dbpath = None
k_vt_col_map = { '':'\x1b[0m', 'default':'\x1b[0m', 'black':'\x1b[30m', 'red':'\x1b[31m', 'green':'\x1b[32m', 'yellow':'\x1b[33m',
	'blue':'\x1b[34m', 'magenta':'\x1b[35m', 'cyan':'\x1b[36m', 'white':'\x1b[37m',
	'bdefault':'\x1b[49m', 'bblack':'\x1b[40m', 'bred':'\x1b[41m', 'bgreen':'\x1b[42m', 'byellow':'\x1b[43m',
	'bblue':'\x1b[44m', 'bmagenta':'\x1b[45m', 'bcyan':'\x1b[46m', 'bwhite':'\x1b[47m' }
vt_cm = k_vt_col_map
def set_vt_col(col):
	sys.stdout.write(k_vt_col_map[col])
def largv_has(keys):
	for i in range(len(keys)):
		 if (keys[i] in largv):
			return True
	return False
def largv_has_key(keys):
	for key in keys:
		ki = largv.index(key) if key in largv else -1
		if (ki >= 0 and ki+1 < len(largv)):
			return True
	return False
def largv_get(keys, dflt):
	if ( hasattr(sys, 'argv')):
		for key in keys:
			ki = largv.index(key) if key in largv else -1
			if (ki >= 0 and ki+1 < len(largv)):
				return largv[ki+1]
	return dflt
def largv_geti(i, dflt):
	if (i >= len(largv)):
		return dflt
	return largv[i]
def init_getch():
	def init_getch_win():
		from msvcrt import getch as win_getch
		return win_getch
	def init_getch_posix():
		import tty,sys,termios
		def posix_getch():
			fd = sys.stdin.fileno(); old_settings = termios.tcgetattr(fd);
			try:
				tty.setraw(sys.stdin.fileno());	ch = sys.stdin.read(1);
			finally:
				termios.tcsetattr(fd, termios.TCSADRAIN, old_settings);
				if ord(ch) == 13:
					return '\n'
				elif ch == '\x1B':
					return [ch, posix_getch(), posix_getch()]
				else:
					return ch
		return posix_getch
	impls = [init_getch_win, init_getch_posix]
	for impl in impls:
		try:
			return impl()
		except:
			#traceback.print_exc()
			pass
	return None
getch = init_getch()
def vt_hist_create():
	return { 'list':[], 'max':30, 'index':0  }
def vt_hist_add(hist, item, max = 30):
	if item not in hist:
		hist.append(item)
	if len(hist) > max:
		hist.remove(0)
def vt_edit(prefix, initial, hist = None):
	inpchars = [x for x in initial]
	while True:
		print '\x1B[2K', '\r{} {}'.format(prefix, ''.join(inpchars)),
		pre_inp = getch()
		#print '[{}]'.format(pre_inp[0] == '\x1B')
		if (len(pre_inp) >= 3 and pre_inp[0:3] == ['\x1B', '[', 'A'] and hist):
			if (hist['index'] >= -len(hist['list'])):
				hist['index'] = hist['index']-1
			if (hist['index'] >= -len(hist['list'])):
				inpchars = [x for x in hist['list'][hist['index']]]
			else:
				inpchars = []
		elif (len(pre_inp) >= 3 and pre_inp[0:3] == ['\x1B', '[', 'B']):
			if (hist['index'] <= -1):
				hist['index'] = hist['index']+1
			if (hist['index'] < 0):
				inpchars = [x for x in hist['list'][hist['index']]]
			else:
				inpchars = []
		if len(pre_inp) == 1:
			if ('\n' in pre_inp):
				sys.stdout.write('\n')
				break
			else:
				for x in pre_inp:
					if x == '\x7F':
						if len(inpchars):
							inpchars.pop()
					else:
						inpchars.append(x)
	return ''.join(inpchars)
def dbGetNode(conn, id):
	ret = []
	recs = conn.execute('SELECT node_id, name FROM nodes WHERE node_id=?', (id,) )
	rec = recs.fetchone(); recs.close(); return rec;
def dbFindNode(conn, name, soft=False):
	ret = []
	recs = conn.execute('SELECT node_id, name FROM nodes WHERE name=?', (name,) )
	rec = recs.fetchone(); recs.close();
	if soft and rec == None:
		nodes = dbGetNodes(conn)
		for n in nodes:
			if name in n[1]:
				return n
	return rec
def dbHasNode(conn, name):
	return dbFindNode(conn, name) != None
def dbGetNodes(conn):
	ret = []
	recs = conn.execute('SELECT node_id, name FROM nodes')
	rec = recs.fetchone()
	while (rec != None):
		ret.append(rec)
		rec = recs.fetchone()
	recs.close()
	return ret
def dbAddNode(conn, node):
	conn.execute("INSERT INTO nodes VALUES (?,?)", (None, node[1] ) )
	conn.commit()
def dbUpdateNode(conn, node):
	conn.execute('UPDATE nodes SET name=? WHERE node_id=?', (node[1], node[0]) )
	conn.commit()
def dbAddEdge(conn, frm, to, tp, descr):
	conn.execute("INSERT INTO edges VALUES (?,?,?,?,?)", (None, frm, to, tp, descr) )
	conn.commit()
def dbUpdateEdge(conn, edge):
	conn.execute('UPDATE edges SET node_frm=?, node_to=?, tp=?, descr=? WHERE edge_id=?', (edge[1], edge[2], edge[3], edge[4], edge[0]) )
	conn.commit()
def dbGetNodeEdges(conn, node_id):
	rets = ([], []); conds = ('node_frm', 'node_to');
	for i in range(len(conds)):
		cond = conds[i]
		recs = conn.execute('SELECT edge_id, node_frm, node_to, type, descr FROM edges WHERE {}=?'.format(cond), (node_id, ) )
		rec = recs.fetchone()
		while (rec != None):
			rets[i].append(rec)
			rec = recs.fetchone()
		recs.close()
	return rets
def dbBootstrap(conn):
	conn.execute('CREATE TABLE nodes(node_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
	conn.execute('CREATE TABLE edges(edge_id INTEGER PRIMARY KEY AUTOINCREMENT, node_frm INTEGER, node_to INTEGER, type TEXT, descr TEXT)')
	conn.commit()
def dbStartSession(dbPath):
	conn = None
	if (dbPath is not None):
		tail, head = os.path.split(dbPath)
		if (not os.path.isdir(tail)):
			os.makedirs(tail)
		conn = sqlite3.connect(dbPath)
		if 1:
			tableListQuery = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY Name"
			cursor = conn.execute(tableListQuery)
			tables = map(lambda t: t[0], cursor.fetchall())
			cursor.close()
			if (len(tables) == 0):
				dbBootstrap(conn)
	else:
		conn = sqlite3.connect(":memory:")
		dbBootstrap(conn)
	return conn
def dbEndSession(conn):
	if conn is None:
		return 0
	conn.close()
def printList(prefix, lst, sep, col1, col2):
	for i in range(len(lst)):
		set_vt_col(col2 if i%2 else col1)
		print '{}{}{}'.format(prefix, lst[i], sep if i+1<len(lst) else ''),
	if len(lst):
		set_vt_col('default')
		print ''
def runInputLoop():
	conn = dbStartSession(g_dbpath)
	try:
		while True:
			inp = vt_edit('>', '')
			#inp = raw_input(); print inp;
			input_splt = inp.split(' ')
			cmd = input_splt[0]
			if cmd == 'q':
				break
			elif cmd == 'a':
				name = ' '.join(input_splt[1:]).strip()
				if dbHasNode(conn, name) == False:
					dbAddNode(conn, [None, name])
			elif cmd == '-':
				try:
					inn = ' '.join(input_splt[1:])
					n1 = inn.split('-')[0].strip()
					n2 = inn.split('-')[1].split(':')[0].strip()
					descr = inn.split('-')[1].split(':')[1].strip()
					in1 = dbFindNode(conn, n1)
					in2 = dbFindNode(conn, n2)
					if in1 != None and in2 != None:
						dbAddEdge(conn, in1[0], in2[0], '-', descr)
				except:
					traceback.print_exc()
			elif cmd == 'l':
				if len(input_splt) > 1:
					try:
						in1 = dbFindNode(conn, input_splt[1].strip(), True)
						edges = dbGetNodeEdges(conn, in1[0])
						e1 = ['{}: {}'.format(dbGetNode(conn, x[2])[1], x[4]) for x in edges[0]]
						e2 = ['{}: {}'.format(dbGetNode(conn, x[1])[1], x[4]) for x in edges[1]]
						printList(' ', e1+e2, '\n', 'white', 'yellow')
					except:
						traceback.print_exc()
				else:
					printList(' ', [x[1] for x in dbGetNodes(conn)], ',', 'white', 'yellow')
	except:
		dbEndSession(conn)
		traceback.print_exc()
		e = sys.exc_info()[0]
		raise e
	dbEndSession(conn)
def main():
	global largv
	global g_dbpath
	largv = sys.argv
	set_vt_col('default'); print '';
	if largv_has(['-db']):
		g_dbpath = largv_get(['-db'], None)
	runInputLoop()
main()
