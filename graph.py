from indexify import indexify_function, Graph, Image

@indexify_function()
def scrape_website(url: str) -> str:
    import requests
    return requests.get(f"http://r.jina.ai/{url}").text

@indexify_function()
def summarize_text(text: str) -> str:
    from openai import OpenAI
    completion = OpenAI().chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Generate a summary of this website"},
            {"role": "user", "content": text}
        ],
    )
    c = completion.choices[0].message.content
    return c

g = Graph(name="website-summarizer", start_node=scrape_website)
g.add_edge(scrape_website, summarize_text)
