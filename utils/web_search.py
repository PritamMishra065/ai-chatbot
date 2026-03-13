from duckduckgo_search import DDGS


def search_web(query):
    """Search the web using DuckDuckGo"""

    results = []

    try:
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=3):
                results.append(r["body"])

        return "\n".join(results)

    except Exception as e:
        return f"Web search error: {str(e)}"