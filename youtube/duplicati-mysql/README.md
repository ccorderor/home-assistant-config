## Backups Seguros de MySQL / MariaDB con Duplicati

Los backups de bases de datos relacionales no deben hacerse copiando directamente los ficheros, y aunque en el caso de una instalación domótica no debería causar excesivos problemas, la solución más adecuada es realizar un dump utlizando las tools que proveen los motores de bases de datos.

En este ejemplo vamos a suponer que hemos montado todo tal y como muestro en el canal de Youtube (https://www.youtube.com/channel/UC2zp7AWsYhZaGmYTjP8hZ7A/), es decir, con docker y docker-compose.

Os dejo un script que podéis añadir en el crontab, y de esa forma, que regularmente se haga un dump de vuestras bases de datos a un directorio específico. Dicho directorio será el que añadáis en la configuración de backup en Duplicati.

Adicionalmente podéis añadir vuestra configuración de BOT en Telegram para que os notifique si se ha hecho correctamente o no el backup.

```
# Directorio donde se van a almacenar los backups
backupfolder=/srv/docker/backup_db/dumps

# Notificación Telegram 
API_KEY="VUESTRO TOKEN"
CHAT_ID=ID_DEL_CHAT

# MySQL/MariaDB config
user=XXXXXXX
password=XXXXXXXX

# Días de rotación de los backups
keep_days=7

sqlfile=$backupfolder/all-database-$(date +%d-%m-%Y_%H-%M-%S).sql
zipfile=$backupfolder/all-database-$(date +%d-%m-%Y_%H-%M-%S).zip 

# Lanzamos la creación del backup
docker-compose -f ../docker-compose.yml exec db /usr/bin/mysqldump -u $user -p$password --all-databases > $sqlfile 

if [ $? == 0 ]; then
  echo 'Backup SQL creado' 
else
  curl -s "https://api.telegram.org/bot$API_KEY/sendMessage?chat_id=$CHAT_ID&text=DB_BACKUP_ERROR" 
  exit 
fi 

# Comprimimos el backup
zip $zipfile $sqlfile 
if [ $? == 0 ]; then
  echo 'Backup comprimido correctamente' 
else
  echo 'ERROR al comprimir el backup'
  curl -s "https://api.telegram.org/bot$API_KEY/sendMessage?chat_id=$CHAT_ID&text=DB_BACKUP_ERROR_2"
  exit 
fi 
rm $sqlfile 
echo $zipfile
curl -s "https://api.telegram.org/bot$API_KEY/sendMessage?chat_id=$CHAT_ID&text=DB_BACKUP_OK!"

# Rotamos backups 
find $backupfolder -mtime +$keep_days -delete
```

Tenéis que copiar este script en algún lugar de vuestro servidor, y añadir una entrada al cron para que se ejecute, del siguiente tipo:

```
15 20 * * * /srv/docker/backup_db/mariadb_backup.sh
```
