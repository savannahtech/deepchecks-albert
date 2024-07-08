#!/usr/bin/env bash

# This script can be used to generate an ".env" for local development with
# docker compose.
#
# Example:
# ./scripts/secrets.sh [--silent | -s]

function check_openssl {
    which openssl > /dev/null
}

function gen_random_string {
    openssl rand -hex 16 | tr -d "\n"
}

function gen_env {
    cat << EOF
#
# USE THIS ONLY LOCALLY
#

# ==============================================================================
# Docker settings
# ==============================================================================

# Variables in this file will be substituted into docker-compose.yml
# Save a copy of this file as ".env" and insert your own values.
#
# Verify correct substitution with:
#
#   docker compose config
#
# If variables are newly added or enabled,
# please restart the images to pull in changes:
#
#   docker compose restart {container-name}
#

# Local Development
APP_DOMAIN=127.0.0.1
APP_URL=http://127.0.0.1


# Default environment variables
APP_ADMIN_PASSWORD=0901d2cb0b747785770f0c713341f527

# Database settings
APP_PGHOST=db
APP_PGPORT=5432
APP_PGUSER=deepcheck_user
APP_PGPASSWORD=3208e3d60c3cef6743c54fd081755881
APP_DB_NAME=deepcheck_db



# Django settings

# Django 4.2 requires at least a 50-char-length secret
DJANGO_SECRET_KEY=d498850e47ff90ce4c7625a0308640ed506ff98044d81bd441e94489a3d95ab5e7fe9dcfb2bdfe9adfg4836364aea3c0c5008ca

DEBUG_TOOLBAR_ENABLED=true
FAIL_FAST=true


EOF
}


check_openssl
RET=$?
if [ $RET -eq 1 ]; then
    echo "Please install 'openssl' >  https://www.openssl.org/"
    exit 1
fi

set -Eeuo pipefail

silent="no"

while [[ $# -gt 0 ]]; do
    case "$1" in
        --silent | -s )
            silent="yes"
            shift
        ;;

        * )
            shift
        ;;
    esac
done





gen_env > .env