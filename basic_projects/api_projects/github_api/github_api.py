import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response
# ? about to pass in an argument, q=(query), 
# language:python means we want info based on python
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print("Status code:" +str(r.status_code))




# Process results.
response_dict = r.json()
print('Total repositries: '+ str(response_dict['total_count']))
# Explore information about the repositries
repo_dicts = response_dict['items']
repo_links, stars, labels  = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    # Use HTML anchor tag to generate the link
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']

    # Plotly lets you use HTML code within text elements
    label = f"{owner}<br />{description}"
    labels.append(label)

# Make plots

data = [{
    'type':'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker' :{
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
    }]

my_layout = {
    'title': 'Most Starred Python Projects on Github',
    'titlefont':{'size': 28},
    'xaxis': {
        'title':'Repositry',
        'titlefont':{'size': 24},
        'tickfont':{'size': 14},
    },
    'yaxis': {
        'title':'Stars',
        'titlefont':{'size': 24},
        'tickfont':{'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')



