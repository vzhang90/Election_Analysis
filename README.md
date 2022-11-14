# Election Analysis

## Project Overview
Tom and Seth require help analyzing election audit results to the election commission. Working from the [election_results file](https://github.com/vzhang90/Election_Analysis/blob/main/Resources/election_results.csv), use conditional & non-conditional statements with membership and logical operators to find the requested results. These results will be printed to the command line and subsequently saved in the text [election_analysis file](https://github.com/vzhang90/Election_Analysis/blob/main/Resources/election_results.csv).

A complete election audit of a recent local congressional electionl to the Colorado Board of Elections employee has been analyzed through Python script to deliver the following information:  
    1. Calculate the total number of votes cast  
    2. Get a complete list of candidates who received votes  
    3. Calculate the total number of votes each candidate received  
    4. Caclualte the percentage of votes each canddiate won  
    5. Determine the winner of the election based on popular vote  
  
## Resources
- Election Results: [election_results.csv](https://github.com/vzhang90/Election_Analysis/blob/main/Resources/election_results.csv)
- Software: Python 3.6.1, Visual Studio Code, 1.38.1  
- Python Script: [Python_Challenge.py](https://github.com/vzhang90/Election_Analysis/blob/main/PyPoll_Challenge.py)

## Results
- Election Analysis: [election_analysis.txt](https://github.com/vzhang90/Election_Analysis/blob/main/analysis/election_analysis.txt)

The analysis of the election show that:
  - There were 369,711 votes in the election
  - The counties were:  
     - Jefferson
     - Denver
     - Arapahoe
   
  - The county results were:
     - Jefferson County received 10.5% of the vote and 38,855 number of votes
     - Denver County receieved 82.8% of the vote and 306,055 number of votes
     - Arapahoe County receieved 6.7% of the vote and 24,801 number of votes
     
  - The county with the largest turnout: Denver
  
  - The candidates were: 
     - Charles Casper Stockham
     - Diane DeGette  
     - Raymond Anthony Doane  
     
  - The candidate results were:
     - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
     - Diane DeGette who received 73.8% of the vote and 272,892 number of votes.  
     - Raymond Anthony Doane received 3.1% of the vote and 11,606 number of votes.  
       
  - The winner of the election was:
     - Diane DeGette who received 73.8% of the vote and 272,892 number of votes.
      

## Election Audit Summary
The attached script [Python_Challenge.py](https://github.com/vzhang90/Election_Analysis/blob/main/PyPoll_Challenge.py) can be used for any election. There could be an additional information added with another stated variable `winning vote difference` to determine by how many votes the winner of the election had more than the candidate with the 2nd highest number of votes.
