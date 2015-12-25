#!/bin/bash

echo "download page view: $(cat ng_access.log | grep 'GET /pub/html/download.html' | wc -l)"

cat ng_access.log | grep 'GET /pub/html/download.html' | awk 'BEGIN{FS=",,"}{refcount[$9]++;count++}END{for(a in refcount)print refcount[a] " " refcount[a]/count*100" "a}' | sort -nr -k1 


# count article page view
echo "article page view: $(cat ng_access.log | grep 'GET /page/news/' | wc -l)"
cat ng_access.log | grep 'GET /page/news/' | awk 'BEGIN{FS=",,"}{refcount[$6]++;count++}END{for(a in refcount)print refcount[a] " " refcount[a]/count*100" "a}' | sort -nr -k1 

