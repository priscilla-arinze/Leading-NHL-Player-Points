# Leading NHL Player Points

Python project inspired by [tutorial exercise](https://github.com/priscilla-arinze/PythonReview/tree/main/EXERCISES/Exercise%20-%20Regular%20Expressions%20%26%20Web%20Crawler%20(2022%20NHL%20Statistics))

* Uses BeautifulSoup library for web scraping
* Uses regular expressions ('re' library) for keyword matching


## TO-DO:
* ~~Mapping/matching team abbreviation dictionary keys to user input (*abbreviations only & static season for now*)~~
    * __DONE__: Functions have been updated to allow for user input for both season and team name abbreviations

<br>

* *Based on above, update functions to be applicable for all NHL teams*
    * __KINDA DONE__: only accounts for the teams that appear on the Covers.com stats page for now, need to do more research for stats for ALL teams

<br>


* DATA VALIDATION:
    * Add condition to check if table of data is null or not (e.g. if the season hasn't started yet)
    * User input for season
    * Case-sensitive for team abbreviation?

<br>

* Once above finally works, allow varied user input (e.g. "ranger", "arizona", etc.) + use list of team name abbreviations & regex to determine which team the user is referring to

* Once everything is functional, consider adding it to website portfolio (scrape for more details/image of players based on player last name & team)
