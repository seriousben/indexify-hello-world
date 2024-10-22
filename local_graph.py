from indexify import Graph
from graph import g

invocation_id = g.run(block_until_done=True, url="https://seriousben.com")
results = g.output(invocation_id, "summarize_text")
print(results)
