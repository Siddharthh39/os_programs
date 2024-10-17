#!/bin/bash

BASE_DIR="/mnt/hgfs/stuff"

echo "Choose an option:"
echo "1) Go to the base directory ($BASE_DIR)"
echo "2) Books"
echo "3) C-Ninjas"
echo "4) Linux Scripts"
echo "5) Patterns"
echo "6) Projects"
read -p "Enter your choice (1-6): " choice

case $choice in
    1)
        subdirectory=""
        ;;
    2)
        subdirectory="books"
        ;;
    3)
        subdirectory="c-ninjas"
        ;;
    4)
        subdirectory="linux_scripts"
        ;;
    5)
        subdirectory="patterns"
        ;;
    6)
        subdirectory="projects"
        ;;
    *)
        echo "Invalid option. Please enter a number between 1 and 6."
        exit 1
        ;;
esac

# If a subdirectory is chosen, append it to the base directory path
if [ -n "$subdirectory" ]; then
    full_path="$BASE_DIR/$subdirectory"
else
    full_path="$BASE_DIR"
fi

if [ -d "$full_path" ]; then
    cd "$full_path" || {
        echo "Failed to change directory to $full_path"
        exit 1
    }
    echo "Changed directory to $full_path"
    ls
else
    echo "Directory $full_path does not exist."
    exit 1
fi
