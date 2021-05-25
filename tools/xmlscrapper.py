import xml.dom.minidom as xdom
import os

output = open("../output_lines.txt", "w", encoding="UTF-8")
output.close()
output = open("../output_lines.txt", "a", encoding="UTF-8")
for x in os.walk(r"C:/Users/Latul/Desktop/xmls"):
    path = (x[0]+"/text.xml").replace("\\", "/")
    try:
        a = xdom.parse(path)
        for b in a.getElementsByTagName("ab"):
            # output.write(b.firstChild.nodeValue)
            output.write(b.firstChild.nodeValue+"\n")
    except FileNotFoundError:
        pass
