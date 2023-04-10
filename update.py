import subprocess
import os
dir_ = os.path.abspath('.')


folder = os.path.join(dir_, 'dist')
li = os.listdir(folder)
if not os.path.exists('data'):
    os.makedirs('data')

for i in li:
    filepath = os.path.join('data', i.split('.')[0]+'.json')

    # with open(filepath, "w") as file:
    #     pass

    subprocess.run(['python', (folder+'/'+i)])