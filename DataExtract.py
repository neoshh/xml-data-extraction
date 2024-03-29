import xml.etree.ElementTree as ET
import xlsxwriter

# import xml data as a tree
tree = ET.parse('data.xml')   # name of xml file to extract (must be same directory as python file)
root = tree.getroot()

# create an empty excel file
workbook = xlsxwriter.Workbook('data.xlsx')   # name of xlsx excel file to save to
worksheet = workbook.add_worksheet()

# iterate through xml tree and write data into excel file
col = 0
for tag in root[0]: 
    worksheet.write(0, col, tag.tag)
    col += 1;

row = 1
col = 0
for child in root:
    for data in child:
        worksheet.write(row, col, data.text)
        col += 1
    col = 0
    row += 1

workbook.close()
