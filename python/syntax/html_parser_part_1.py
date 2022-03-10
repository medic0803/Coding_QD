import re
class Parser:
    def removeComment(self):
        # remove <!-- comment -->
        self.oneline = re.sub("<!--.*?-->", ' ', self.oneline)

    def extractTag(self):
        # find <tag>
        self.tags = re.findall("(?<=<).*?(?=>)", self.oneline)

    def parseAttr(self, raw_attributes):
        if raw_attributes != '':
            # find attri-attri_attri="attri, attri attri"
            attributes = re.findall("\S+=[\'\"].*?[\'\"]|\S+", raw_attributes)
            for attri in attributes:
                print("-> " + attri.split('=', 1)[0] + " > " + attri.split('=', 1)[1][1:len(attri.split('=', 1)[1]) - 1] if '=' in attri else "-> " + attri + " > " + "None")
    def parseTag(self):
        for tag in self.tags:
            if str(tag).endswith('/'):
                if str(tag).endswith('/'):
                    print("Empty : " + tag[:len(tag)-2].split()[0])
                    self.parseAttr(tag[len(str(tag).split()[0]) + 1 : len(tag)-2])
            elif str(tag).startswith('/'):
                print("End   : " + tag[1:])
            else:
                print("Start : " + str(tag).split()[0])
                self.parseAttr(tag[len(str(tag).split()[0]) + 1 :])



    def __init__(self, lines):
        self.oneline = ''.join(lines)
        self.removeComment()
        self.extractTag()
        self.parseTag()

if __name__ == '__main__':
    rows = int(input())
    Parser([input() for x in range(rows)])
