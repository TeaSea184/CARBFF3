#!/bin/bash

# Define the remote server, user, and password
REMOTE_USER="your_username"
REMOTE_HOST="remote_host_address"
PASSWORD="your_password"

# Log onto the remote server
sshpass -p "$PASSWORD" ssh "$REMOTE_USER@$REMOTE_HOST"
#move zip file
scp -r output/${MOLECULE}.zip/ REMOTE_USER@REMOTE_HOST://home/clstay002/Simulations/${MOLECULE}

