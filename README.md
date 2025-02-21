# analysis-action-py

For use if you want to run a python script on every push then save the results to another branch. The idea is to keep any analysis files on a different branch so that the main branch does not have any analysis files.

## How to use
The `.github/workflows/github-actions-py/analysis.py` file contains any analysis that is run on the commit. It stores the result to a file called `<git commit hash>-analysis.txt` which is committed to the `analysis` branch 
