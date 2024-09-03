# How to use a Raspberry Pi

The raspberry pi is a cool little microcontroller you can use for all sorts of projects. I haven't quite a found a use case for it yet, but I learnt some stuff while setting it up, so thought I would share :)

Will keep adding as i learn more!

Connecting to raspberry pi

ssh user@ip address

Sending files

- From computer to raspberry pi

scp /path/to_file user@ip_address:/destination/folder

Send recursively

scp -r /path/to_file user@ip_address:/destination/folder

Raspberry pi to computer

scp user@ip_address:/source/folder destination/folder

mysql -u root -p -e "SHOW DATABASES;"    

USE DATABASE_NAME;

SHOW TABLES;

SELECT * FROM TABLE_NAME;

