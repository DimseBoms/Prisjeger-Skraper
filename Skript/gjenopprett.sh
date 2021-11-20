# Skriptet skal gjenopprette data etter at systemet har blitt gjenopprettet.
# MÃ¥ kjÃ¸res som root.

# Pakker ut data
tar -xvf ~/backup.tar.gz ~/

# Gjenoppretter pakkelister
apt-key add ~/backup/data/Repo.keys 
cp -R ~/backup/data/sources.list* /etc/apt/ 
apt update 
apt install dselect 
dselect update 
dpkg --set-selections < ~/backup/data/Package.list 
apt dselect-upgrade -y

#restore database
mysql < ~/backup/data/mysql.sql