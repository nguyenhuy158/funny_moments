#!/bin/bash

# push source code (main branch)
git add .
git commit -m "update site content"
git push origin main

# build site
hugo

# vào thư mục public
cd public

# init git trong public/
git init
git remote add origin git@github.com:nguyenhuy158/funny_moments.git
git checkout -b gh-pages

# commit & push
git add .
git commit -m "deploy"
git push -f origin gh-pages

# quay lại root
cd ..

