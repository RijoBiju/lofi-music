from youtube_search import YoutubeSearch

def search_youtube(query, max_results=1):
    results = YoutubeSearch(query, max_results=max_results).to_dict()
    return results[0]["url_suffix"]