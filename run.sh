#!/bin/bash

sudo apt-get update
sudo apt-get install -y python docker-compose
sudo usermod -aG docker $USER

echo " [[ UPDATED && INSTALLED ]] "