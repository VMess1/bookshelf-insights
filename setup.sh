#!/bin/bash

# Setup a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create env file for personal input variables
touch .env

# Ask for user details to save to .env file
read -p "Enter your API key: " API_KEY
read -p "Enter your Google Books user ID: " USER_ID

# Write API key and UID to .env file
echo "API_KEY='$API_KEY'" > .env
echo "USER_ID='$USER_ID'" >> .env

# Adding PYTHONPATH env variable
export PYTHONPATH=$PYTHONPATH:$(pwd)
