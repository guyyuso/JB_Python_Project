#!/bin/bash
# Installing nginx on a machine instance based on its name.

vm_name=$1

timestamp() {
    date '+%Y-%m-%d %H:%M:%S'
}

if [[ ! -z $vm_name ]]; then
    echo "$(timestamp) - Starting Nginx installation on '$vm_name'..." 
    sleep 2  # Simulate installation
    echo "$(timestamp) - Installation successful on '$vm_name'." 
else
    echo "$(timestamp) - Error: Please pass vm_name as an argument." 
    exit 1
fi
