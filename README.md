# jupyterkg
Jupyter Widgets interface for browsing Wikidata knowledge graphs.

This notebook demonstrates how to bring up Wikidata Query
knowledge graphs without needing to know anything about the SPARQL
query language. By selecting items from a list, you can generate knowledge
graphs from the Wikidata Query SPARQL endpoint.

The prototype is designed around show depicted content from artists in particular collections, but this is a generic system that can used to assemble any type of query.

* Main execution module: kg-browser-modular.ipynb

![](https://github.com/fuzheado/jupyterkg/blob/main/jupyterkg-screenshot.png)

## Background
The idea for creating this tool was initially inspired by this post by Martin Poulter, Wikimedian In Residence at Oxford University. 
http://blogs.bodleian.ox.ac.uk/digital/2019/01/23/making-wikidata-visible/

Since then, the Wikidata GLAM community has been experimenting with different ways of making these graphs more functional. At The Met, we created a number of graphs to show the connectedness of objects in their historical context. An example related to "Portrait of Madame X" can be seen at: https://w.wiki/BUA

## Credits
Created by User:Fuzheado on Wikidata.

## Running
There are a number of ways to execute this in a runtime environment:

### Via MyBinder
MyBinder is a free service for running Jupyter notebooks in the cloud.

* MyBinder and Voila:
https://mybinder.org/v2/gh/fuzheado/jupyterkg/HEAD?urlpath=voila%2Frender%2Fkg-browser-modular.ipynb
  * Full graphical runtime interface. This may take a minute or so to start up, since it is provisioning a new container and starting up a new Python environment. Short link: http://bit.ly/jupyterkg-mybinder

* MyBinder:
https://mybinder.org/v2/gh/fuzheado/jupyterkg/main?filepath=kg-browser-modular.ipynb
  * A full Jupyter notebook system. Execute by hitting the "Run" button on the first cell. This may take a minute to start up the entire Python/Jupyter environment.

### Via PAWS on Wikimedia servers
You can test these out as well by using the Wikimedia PAWS system,
which is a Jupyter deployment for anyone with a Wikimedia/Wikipedia
account. Link: https://paws.wmcloud.org/

* If you are logged in to PAWS, the following link will pull this Github repo into your PAWS user directory so you can execute it there.
  * https://hub.paws.wmcloud.org/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Ffuzheado%2Fjupyterkg&urlpath=tree%2Fjupyterkg%2Fkg-browser-modular.ipynb&branch=main

* You can start the graphical user interface immediately like a web app, with this Voila link:
  * https://hub.paws.wmcloud.org/user/user-redirect/voila/render/jupyterkg/kg-browser-modular.ipynb
