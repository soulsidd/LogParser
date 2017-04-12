import re, linecache

mainlist = []
def getlist():

     keyexpr = [ r'(?P<IP>\S+)', r'\S+', r'(?P<User>\S+)', r'\[(?P<TimeStamp>.+)\]',
     r'"(?P<RequestType>.+)"', r'(?P<RequestStatus>[0-9]+)', r'(?P<SizeOf>\S+)', r'"(?P<Ref>.*)"',
     r'"(?P<OSys>.*)"', ]
     exp = re.compile(r'\s+'.join(keyexpr) + r'\s*\Z')
     log = open("access.log", "r")
     lines = log.readlines()
     for line in lines:
          comp = exp.match(line)
          pair = comp.groupdict()
          mainlist.append(pair)

def opt1():
     i = 0
     IP = {}
     for line in mainlist:
          raw = mainlist[i]
          if len(raw["IP"]) > 4:
               IP[i + 1] = raw["IP"]
          else:
               IP[i + 1] = "Not Found"
          i = i + 1
     match = []
     try:
          value = raw_input("Enter IP Address To Search  : ")
          for line, ip in IP.items():
               if ip == value:
                    match.append(line)
          return match
     except:
          print "There is problem with given IP Addresses..!!"

def opt2():

     i = 0
     P = []
     for line in mainlist:
          raw = mainlist[i]
          P.append("".join(re.findall(r'\S+$', raw["RequestType"])))
          i = i + 1
     match = []
     i = 0
     try:
          value = raw_input("Enter opt2 To Search  :  ")
          while i < len(P):
               if P[i] == value:
                    match.append(i + 1)
               i += 1
          return match
     except:
          print "There is problem with given opt2"

def opt3():

     i = 0
     OS = []
     for line in mainlist:
          raw = mainlist[i]
          OS.append(getos(raw["OSys"]))
          i = i + 1
     match = []
     i = 0
     try:
          value = raw_input("Enter OS Name To Search  :  ")
          while i < len(OS):
               if OS[i] == value:
                    match.append(i + 1)
               i += 1
          return match
     except:
          print "There is problem with given OS"


def getos(OS):
     try :
          OS = OS.split("(", 1)[1]
          OS = OS.split(";", 1)[0]
     except:
          OS = "Not Found"
     return OS

def choice():
     if mainlist:
          ch = input("Enter 1 To Find Specific IP : \nEnter 2 To Find Specific opt2 : \nEnter 3 To Find Specific OS : ")
          if(ch == 1):
               lst = opt1()
          elif(ch == 2):
               lst = opt2()
          elif(ch == 3):
               lst = opt3()
          else:
               print "Invalid Choice..!"
          save(lst)

def save(matchlist):

     op = open("Results.txt", "a")
     op.write("\n\n\tReport Generated For Specified Custom Search\n\tRetrived " + str(len(matchlist)) + " Lines Of Data")
     for i, lineInd in enumerate(matchlist):
          op.write(str("Line Numbers - " + lineInd + " of input file contains desired output"))
          op.write(str(linecache.getline("access.log", lineInd)))
     print ("\n\tPlease Refer Result.txt file in same directory for output..!")

getlist()
choice()
