# analysis-action-py

For use if you want to run a python script on every push then save the results to another branch. The idea is to keep any analysis files to a different branch so that the main branch does not have any analysis files.

## How to use
The `update.py` file contains any analysis that is run on the commit. It stores the result to a file called `my_text_out.txt` which is committed to the `analysis` branch 
