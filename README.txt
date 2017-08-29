
# use the input file "input" in the HolsteinScripts directory (not in bin directory)

#HOW TO USE GIT!!!
#to make changes and push them to the online repository:
    git add -A
    git commit -m "new commit message"
    git push -u origin master
#to pull the newest version of git from the online repository:
    git fetch origin master
    git reset --hard FETCH_HEAD
    git pull  ?? if needed


#how to prepare jobs on sherlock
## run script for walltime estimator local computer and upload to bin directory!!!!
## make the mu_map in ipynb local computer and upload to bin directory
## run make_mu_map.py with appropriate changes
## create inputfiles and outputfiles folders
## create multiple submit scripts with py script
## submit the jobs
