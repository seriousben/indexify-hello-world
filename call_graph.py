from indexify import RemoteGraph
from graph import g

graph = RemoteGraph.by_name(name="website-summarizer", server_url="http://localhost:8900")
invocation_id = graph.run(block_until_done=True, url="https://en.wikipedia.org/wiki/Golden_State_Warriors")
results = graph.output(invocation_id, "summarize_text")
print(results)
