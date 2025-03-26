#!/bin/bash
# Script to set up Git LFS for large files

# Install Git LFS if not already installed
echo "Installing Git LFS..."
git lfs install

# Track the large file
echo "Tracking large file with Git LFS..."
git lfs track "browser_use_venv/lib/python3.11/site-packages/playwright/driver/node"

# Add .gitattributes to Git
echo "Adding .gitattributes to Git..."
git add .gitattributes

# Add the large file to Git LFS
echo "Adding large file to Git LFS..."
git add "browser_use_venv/lib/python3.11/site-packages/playwright/driver/node"

# Commit the changes
echo "Committing changes..."
git commit -m "Convert large file to Git LFS"

echo "Changes committed successfully. Now you can push with:"
echo "git push origin main"
