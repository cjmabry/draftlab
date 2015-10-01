# draftlab
Python scripts to gather and compile DFS data into usable spreadsheets.

# Install
1. (Optional) Set up a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) and activate it.
2. Navigate to the root directory and install required dependencies

  ```
  pip install -r requirements.txt
  ```
3. Run it

  ```
  python main.py
  ```

# What does it do?
* **main.py** - Scrapes DraftKings player data and combines it with NFL stats, vegas spreads, and FantasyPros.com projections to generate CSVs by position. It is not yet optimized for speed so may take a long time. 

  > *__Note:__* Currently hardcoded to use week 4 Draft Kings player data. Vegas odds and Fantasy Pros projections are scraped for whataver data is currently live on those sites.
* **qb_analysis.py** - Gets NFL stats for qb passes. Currently counts passes by distance and side of field, but can be expanded to be much more powerful. Will be implemented in main app to help predict things such as receiver targets by position and where runningbacks usually run.
