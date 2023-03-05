
# Opsgenie Analyser

This module helps you analyse Opsgenie alerts, and find the most common alerts and monitors. This is helpful if you get a lot of non - essential alerts which get resolved quickly. Opsgenie Analyser takes the csv alert file downloaded from Opsgenie as an input and provides the following functionalities.


* Group by Monitor
* Group by Facet

It shows a pie chart distribution of the alerts grouped by monitor or facet. The facets that are supported are automatically detected by the module based on the input file. 


## How to use it

1. Download the CSV File from Opsgenie 

<img width="1405" alt="Screenshot 2023-03-05 at 17 21 07" src="https://user-images.githubusercontent.com/89913154/222972650-3bf3a163-3f4e-43dc-90a6-7626448826d9.png">

2. Git Clone Repo.

3. Run command ```pip install -r requirements.txt``` from root.

4. Run command ```python main.py "/path/to/opsgenie/filename.csv"``` from root.
## Example 

### Group By Monitor

```
$ python main.py ~/Downloads/finalAlertData.csv
    <<<< Enter >>>> 
    0 -> Group by Monitor 
    1 -> Group by Facets 
$ 0


```
Output 

<img width="777" alt="Screenshot 2023-03-05 at 17 26 17" src="https://user-images.githubusercontent.com/89913154/222972928-69442e52-670b-482d-9997-574bec1c0feb.png">



### Group By Monitor

```
$ python main.py ~/Downloads/finalAlertData.csv
    <<<< Enter >>>> 
    0 -> Group by Monitor 
    1 -> Group by Facets 
$ 1 
$ Found the following Facets:
    {'cluster', 'http.url_details.querystring.brand', 'database'}
    Which facet do you want to group by? 
$ cluster

```
Output

<img width="864" alt="Screenshot 2023-03-05 at 17 29 11" src="https://user-images.githubusercontent.com/89913154/222973085-cc6879c7-66f9-45d5-95c9-2e06615ed21f.png">
