# Internet-Speed-Testing

# All of the following are run on a Raspberry Pi 4

The Rpi4 hosts a MariaDB MySQL database which stores data collected by the python script. The Rpi4 also hosts an apache webserver which is used as a frontend to display the speed test data contained in the database. A python script (set to run at a regular interval stated in RPI cron task scheduling) runs an internet speed test on the network it is connected to. It collects the download speed, upload speed, ping, host server, and the time the test took place. This data is then inserted into the database's datatable for later use by the frontend. The webserver contains a PHP file used to display the data in an organized table for easy analysis. The database can contain up to 100 speed test entrys until the datatable is archived in a CSV file, wiped, then inserted with the new value. The CSV file is saved to a folder within the webserver. These archived files can be accessed and downloaded through the FTP server hosted on the Rpi. 

-- Archived
