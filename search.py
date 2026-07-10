from ddgs import DDGS

def search_web(query, max_results=3):
    """
    Search the web and return a list of results.
    """

    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=max_results))

    return results


def format_results(results):
    """
    Convert search results into text that the AI can read.
    """

    text = ""

    for result in results:
        text += f"""
Title: {result['title']}
Body: {result['body']}
URL: {result['href']}

"""

    return text
