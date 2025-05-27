termux-setup-storage
apt-get install python3 && apt-get install git && apt-get install pip && pip install -r req.txt
mkdir -p $HOME/../opt
mv $HOME/KANGA-HACK/*.py $HOME/../opt/
mv KANGA $HOME/../usr/bin/KANGA
chmod +x $HOME/../usr/bin/KANGA
cd
rm -rf KANGA-HACK
