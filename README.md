# indexify-hello-world

hello world example using openai, indexify-server 0.2.3, indexify 0.2.17, and poetry.

## Setup

1. Instal poetry
1. Export your openai api key in the OPENAI_API_KEY environment variable.

## Local run

1. `python local_graph.py`: Runs the graph locally for local testing and debugging.

## Remote run

1. Setup two terminals opened in the poetry managed virtualenv
1. Terminal 1: `indexify-cli server-dev-mode` -> Starts the indexify server with the python executor.
1. Terminal 2: `python deploy_graph.py` -> Deploy the graph definition on the indexify server.
1. Terminal 2: `python call_graph.py` -> Executes the graph remotely on the indexify-server and executor.
