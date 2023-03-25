import subprocess
import os
dir_ = os.path.abspath('.')

folder = os.path.join(dir_, 'dist')
li = os.listdir(folder)
if not os.path.exists('data'):
    os.makedirs('data')

test = False


for i in li:
    filepath = os.path.join('data', i.split('.')[0]+'.json')
    print(i)
    with open(filepath, "w") as file:
        pass
    if not test:
        subprocess.run(['python', (folder+'/'+i)])


while test:
    userinpt=input("file: ")
    if userinpt == 'done':
        break
    subprocess.run(['python', (folder+'/'+userinpt+'.py')])
    