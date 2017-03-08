'''
        file = open('text.txt','w')
        file.write(self.uuid.get('uuid'))
        file.close()
        '''
        
import re
rex = r'[a-zA-Z0-9]=='
file = open('text.txt','w')
lines = file.readlines()
for i in range(len(lines)):
    print lines[i]