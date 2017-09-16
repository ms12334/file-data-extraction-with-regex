import re

with open('result.log','a') as fout:
    with open('Consumer_Complaints.csv','r') as fin:
        for line in fin: 
            if re.search(r'([^,]*?),("[^"]*?"|[^,]*?),([^,]*?),([^,]*?),([^,]*?),([^,]*?),([^,]*?),([^,]*?),([0-9]*?)\n', line):
                result = re.sub(r'([^,]*?),("[^"]*?"|[^,]*?),([^,]*?),([^,]*?),([^,]*?),([^,]*?),([^,]*?),([^,]*?),([0-9]*?)\n', r'\1,\9\n', line)
                result = re.sub(r'^(.*?),([^,]*?),([0-9]*?)\n', r'\2,\3\n', result)
                if re.match('[0-9]{5},[0-9]*?', result) == None:
                    fout.write(result)
