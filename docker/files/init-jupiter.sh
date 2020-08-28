#!/bin/sh

# TODO: add conditional initialization that depends on environment variables for example

jupyter notebook --generate-config

# jupiter configuration
echo "c.NotebookApp.ip = '*'"               >> /root/.jupyter/jupyter_notebook_config.py
# echo "c.NotebookApp.port = 8888" >> /root/.jupyter/jupyter_notebook_config.py
echo "c.NotebookApp.token = ''"             >> /root/.jupyter/jupyter_notebook_config.py
