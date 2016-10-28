#!/usr/bin/env bash
set -e

# enable source URIs so that `apt-get build-dep` works properly
cp /etc/apt/sources.list /etc/apt/sources.list.d/dev-sources.list
sed -i 's/deb /deb-src /g' /etc/apt/sources.list.d/dev-sources.list

# install our system-level and project requirements
echo "Installing system-level requirements..."
apt-get -qq update
apt-get install --no-install-recommends -qqy postgresql > /dev/null
apt-get build-dep --no-install-recommends -qqy pillow psycopg2 > /dev/null
pip -q install -r requirements.txt

# start cache & database
service postgresql start

# initialize the db
echo "CREATE USER wickwockpy WITH PASSWORD 'wickwockpy'; CREATE DATABASE wickwockpy OWNER wickwockpy; ALTER USER wickwockpy CREATEDB;" | su postgres -c psql
python manage.py migrate