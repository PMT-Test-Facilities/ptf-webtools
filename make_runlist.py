#!/bin/env python
import csv

outfile = open('/home1/midptf/online/custom/runlist.html','w')
outfile.write(
    "<!DOCTYPE html>\n "
    " <html>\n "
    "\n"
    "<head>\n"
    "<style>\n"
    "table {\n"
    "    width:100%;\n"
    "}\n"
    "table, th, td {\n"
    "    border: 1px solid black;\n"
    "    border-collapse: collapse;\n"
    "}\n"
    "th, td {\n"
    "    padding: 5px;\n"
    "    text-align: left;\n"
    "}\n"
    "table#nicetable tr:nth-child(even) {\n"
    "    background-color: #eee;\n"
    "}\n"
    "table#t01 tr:nth-child(odd) {\n"
    "   background-color:#fff;\n"
    "}\n"
    "table#nicetable th{\n"
    "    background-color: black;\n"
    "    color: white;\n"
    "}\n"
    "</style>\n"
    "</head>\n"
    "\n"
    "<body>\n"
    "\n"
    "<br>\n")

with open('/home1/midptf/online/custom/runs.txt','r') as f:
    reader = csv.reader(f,delimiter='\t')
    outfile.write('<table id="nicetable">\n')
    for line in reader:
        if len(line) == 0:
            continue
        if 'Run' in line[0]:
            outfile.write('  <tr>\n')
            for i in range(len(line)):
                if i in [2,3,5,6,11]:
                    continue
                #hack:
                if i == 10:
                    new_line = line[i].split()
                    outfile.write('    <th>%s</td>\n'%new_line[0])
                    outfile.write('    <th>%s %s</td>\n'%(new_line[1],new_line[2]))
                    outfile.write('    <th>%s</td>\n'%(new_line[3]))
                else:
                    outfile.write('    <th>%s</td>\n'%line[i])
            outfile.write('  </tr>\n')
        
        elif '-' not in line[0]:
            outfile.write('  <tr>\n')
            for i in range(len(line)):
                if i in [4,6,8,10,12]:
                    continue
                outfile.write('    <td>%s</td>\n'%line[i])
            outfile.write('  </tr>\n')
    outfile.write('</table>\n')
outfile.write("</body>\n"
              "</html>\n")
