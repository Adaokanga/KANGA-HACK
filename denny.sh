termux-setup-storage
apt-get install python3 && apt-get install git && apt-get install pip && pip install -r req.txt && pkg install unzip
unzip KANGA-HACK.zip -d KANGA-HACK
mkdir -p $HOME/../opt
mv $HOME/KANGA-HACK/KANGA-HACK/KANGA $HOME/../usr/bin/KANGA
chmod +x $HOME/../usr/bin/KANGA
mv $HOME/KANGA-HACK/KANGA-HACK $HOME/../opt/
cd
rm -rf KANGA-HACK
cd 
rm -rf KANGA-HACK
