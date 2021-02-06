import sys, getopt
def makerow(string, tag):
    out = '<tr>'
    for i in string.split(","):
        out+= tag+i+tag[0]+"/"+tag[1:]
    out+= "</tr>"
    return out

def maketable(inputfile, outputfile):
    f = open(inputfile, "r")
    of = open(outputfile, "w")
    of.write('<table style = "border: 1px solid black;">')
    of.write(makerow(f.readline(), "<th>"))
    for line in f:
        of.write(makerow(line, '<td  style = "border: 1px solid black;">'))
    
    of.write("</table>")
    print ('Input file is ', inputfile)
    print ('Output file is ', outputfile)
    f.close() 
    of.close()

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hji:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print ('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('main.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   maketable(inputfile, outputfile)


if __name__ == "__main__":
   main(sys.argv[1:])