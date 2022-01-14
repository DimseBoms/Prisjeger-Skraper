# Skriptet skal oppdatere all relevant data på systemet. Originalt hentet fra internett og modifisert.
# Kjøres en gang om dagen ved midnatt og oppdaterer til Google Drive. Det oppbevares max 14 dager med backups.
# Kilde: 'https://sqlbak.com/blog/automatic-backup-of-raspberry-pi-to-any-cloud'

# Henter dato
dato=`date +%F`

# re-create a backup directory
rm -rf ~/backup
mkdir -p ~/backup/data

# create a database's dump
mysqldump --all-databases > ~/backup/data/mysql.sql

# copy a package list
dpkg --get-selections > ~/backup/data/Package.list
cp -R /etc/apt/sources.list* ~/backup/data
apt-key exportall > ~/backup/data/Repo.keys

# compress directories
tar -czf ~/backup/backup.tar.gz /home /etc /usr/local/etc ~/backup/data

# delete old backups
rclone delete drive:/backups/ --min-age 14d

# send to the cloud
rclone copyto ~/backup/backup.tar.gz drive:/backups/backup_$dato.tar.gz

# delete the temporary directory
rm -rf ~/backup
.
