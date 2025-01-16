# influxdb/init.sh
#!/bin/bash
influx -execute "CREATE DATABASE capteur_bucket"