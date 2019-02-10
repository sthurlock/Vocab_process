import sys
import re
from subprocess import call

def get_list(part,line):
    newline = line.replace(", ", ",")
    m = re.match(part + " (.*)$", newline)
    count=0
    if m:
       thelist = m.group(1)
       print("** " + part)
       for word in thelist.split(","):
          print(word + ":")
          count = count + 1
    return count

tags = ["Synonyms:", "Phrases:", "Related Phrases:", "Related Forms:", "Antonyms:" ]

inputfile = sys.argv[1]
print("-" * 20)
file = open(inputfile, 'r')
for line in file:
    result = re.search("^([0-9]+[.]) +([^ ]+) +(.*)$", line)
    if result:
       word_num = result.groups()[0] 
       word = (result.groups()[1]).replace('-',"" ) 
       word_type = result.groups()[2] 
       print(word_num, word, word_type)
       continue

    def_match = re.match("Definition[0-9]*: (.*)$", line) 
    if def_match:
       definition = def_match.groups()[0]
       print(line, end='')
       continue

    for tag in tags:
       if (get_list(tag, line) > 0):
          break
