#!/usr/bin/env bash

# Memo
# Run on server: Crontab
# 00:10 at every Monday
# 10 0 * * 1 sh /opt/logs/log-rotate.sh ng_access.log > /dev/null 2>&1

if [ $# -lt 1 ]; then
    echo 'Usage: <cmd> <log-file-name>'
    exit 1
fi

SOURCE_LOG_FILE=$1;shift
TARGET_LOG_FILE="${SOURCE_LOG_FILE}.$(date +%Y%m%d -d last-day)"

# Step into script directory
cd $(dirname $0)

# Rotate current log file
#cp -b ${SOURCE_LOG_FILE} ${TARGET_LOG_FILE}
mv -b ${SOURCE_LOG_FILE} ${TARGET_LOG_FILE}

# Restart nginx to write log correctly
kill -HUP $(cat /opt/conf/nginx/nginx.pid)
#/opt/sysapp/nginx/sbin/nginx -s reload

# Count 
# python count.py ${TARGET_LOG_FILE} > "r.$(date +%Y%m%d -d last-day)" 

# TODO: Gen UV/PV info
# 
