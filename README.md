Just another one python project for test purposes with "all in one executable" packages.

**Prerequisites**

```
pip install -r requirements.txt
```

**Usage**

```
python main.py -t hostname
```

**Pyinstaller**

```
pip install pyinstaller
pyinstaller -F main.py
./dist/main -t localhost
```

**Nuitka**

```
pip install nuitka
sudo dnf install -y upx
python -m nuitka --follow-imports main.py
upx -9 -o main.bin.packed main.bin
./main.bin.packed -t localhost
```
