#!/usr/bin/python

#sudo pip install xlrd
#sudo pip install panda
import xlrd
import pandas as pd

def pg150ultrascalememoryippdf():
	workbook = xlrd.open_workbook('pg150-ultrascale-memory.xlsx')
	worksheet = workbook.sheet_by_index(0);
	flag = 0;
	output = open("pg150.h", "w+")
	output.write("#ECC Register Memory Map\n");
	#row = worksheet.row(0)
	for row in range(0, worksheet.nrows):
		cell_obj = worksheet.cell(row, 0)
		if (cell_obj.value == "NAME"):
			flag = 1
		elif (flag) and (cell_obj.value != xlrd.empty_cell.value) :
			output.write("#Description: " + worksheet.cell(row, 2).value + "\n")		
			output.write("#define " + cell_obj.value + "\t" + worksheet.cell(row, 1).value + "\n")		
			print('(%s) value %s' %(row, cell_obj.value)) 

	output.close()
	return

pg150ultrascalememoryippdf()
