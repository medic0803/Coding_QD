import re
class Parser:
    def removeComment(self):
        self.oneline = re.sub("<!--.*?-->", ' ', self.oneline)

    def extractTag(self):
        # self.oneline = re.sub("<\w*>", '')
        self.tags = re.findall("<.*?>", self.oneline)
        self.tags = re.findall("(?<=<).*?(?=>)", self.oneline)
        # print(self.tags)
    def parseTag(self):
        for tag in self.tags:
            if str(tag).endswith('/'):
                print("Empty : " + tag[:len(tag)-2])
            elif str(tag).startswith('/'):
                print("End   : " + tag[1:])
            else:
                attrTag = str(tag).split()
                print("Start : " + attrTag[0])
                if len(attrTag) > 1:
                    for attri in attrTag[1:]:
                        if '=' in attri:
                            print("-> " + attri.split('=')[0] + " > " + ((attri.split('=')[1])[1:len(attri.split('=')[1]) - 1]))
                        else:
                            print("-> " + attri.split('=')[0] + " > " + "None")


    def __init__(self, lines):
        # put in oneline, to
        self.oneline = ''.join(lines)
        # print(self.oneline)
        # print(re.findall("<!--.*?-->", self.oneline))
        self.removeComment()
        self.extractTag()
        self.parseTag()

        # print(self.oneline)


# rows = int(input())
# Parser([input() for x in range(rows)])

if __name__ == '__main__':
    # lines = ["<start atasdfde><starT attribute=\"test\">","<value attribute='233'>","<!-- </end>","<empty />--></end><Inside /> <!-- <script>-->"]
    # Parser(lines)
    rows = int(input())
    Parser([input() for x in range(rows)])
