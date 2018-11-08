elemInLine = 81

# function to identify the element
def typeIndex(line):
    if line.find('-') == 0: return "element"

    first = line.find('.')
    second = line.find('.', first+1)

    if second == -1: return "title"
    else: return "subtitle"

def writeBar(name, type):
    bar = "/*"
    bar = bar + type*28 + ' '
    bar = bar + name[:-1] + ' '
    length = elemInLine - len(bar) - 2
    bar = bar + type*length + '*/' + '\n\n'
    return bar

# write the lines by type
def writeLine(line, writeFile):
    type = typeIndex(line)
    bar = ""
    if type == "title":
        bar = writeBar(line, '=')
    elif type == "subtitle":
        bar = writeBar(line, '*')
    elif type == "element":
        space = line.find(' ')
        name = line[space+1:-1]
        bar = ".{} ".format(name)
        bar = bar + '{' + '\n\n}\n\n\n'
    writeFile.write(bar)




# ============ MAIN ==================
# open files
file = "myStyle"
index = open("{}.txt".format(file), "r")
fileCSS = open("{}.css".format(file), "w")

for line in index:
    print line,
    writeLine(line, fileCSS)
    print ""
