import subprocess

for i in range(10):
    subprocess.call(f'git add /Users/chanwutk/Desktop/2024-05-23-24--Diablo-Lake/DSCF0?{i}?.JPG')
    subprocess.call(f'git commit -m "{i}"')
    subprocess.call(f'git push')