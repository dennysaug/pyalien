#!/bin/bash

#apt-get install -y libnspr4 libnss3  && \
#
#dpkg -i google-chrome-stable_90.0.4430.93-1_amd64.deb && \
#apt --fix-broken install && \

if [ ! -f "$PWD/non-install" ]; then
    pip install --no-cache-dir -r requirements.txt && \
    apt-get update && \
    apt-get install -y chromedriver xdg-utils fonts-liberation python-mysqldb adwaita-icon-theme dconf-gsettings-backend dconf-service distro-info-data glib-networking glib-networking-common glib-networking-services gsettings-desktop-schemas libappindicator3-1 libatk-bridge2.0-0 libcolord2 libdbusmenu-glib4 libdbusmenu-gtk3-4 libdconf1 libegl1-mesa libepoxy0 libgbm1 libgtk-3-0 libgtk-3-bin libgtk-3-common libindicator3-7 libjson-glib-1.0-0 libjson-glib-1.0-common libproxy1v5 librest-0.7-0 libsoup-gnome2.4-1 libsoup2.4-1 libwayland-client0 libwayland-cursor0 libwayland-egl1-mesa libwayland-server0 libxcb-xfixes0 libxkbcommon0 lsb-release xkb-data && \
    wget https://chromedriver.storage.googleapis.com/90.0.4430.24/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    rm -rf chromedriver_linux64.zip && \
    wget https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_90.0.4430.93-1_amd64.deb && \
    dpkg -i google-chrome-stable_90.0.4430.93-1_amd64.deb && \
    rm -rf google-chrome-stable_90.0.4430.93-1_amd64.deb && \
    echo "\n\n\tFinish install\n\n" && \
    touch non-install
fi

python main.py

#echo " F I M "


#docker rmi $(docker images -q)