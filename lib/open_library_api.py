import requests
import json


class Search:

    def _build_url(self, search_term):
        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1
        return f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"

    def get_search_results(self):
        search_term = "the lord of the rings"
        URL = self._build_url(search_term)
        
        try:
            response = requests.get(URL)
            response.raise_for_status()
            return response.content
        except requests.RequestException as e:
            return f"Error fetching data: {e}".encode()

    def get_search_results_json(self):
        search_term = "the lord of the rings"
        URL = self._build_url(search_term)
        print(URL)
        
        try:
            response = requests.get(URL)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": f"Error fetching data: {e}"}

    def get_user_search_results(self, search_term):
        URL = self._build_url(search_term)
        
        try:
            response = requests.get(URL)
            response.raise_for_status()
            data = response.json()
            
            if not data.get('docs') or len(data['docs']) == 0:
                return "No results found for the given search term."
            
            doc = data['docs'][0]
            title = doc.get('title', 'Unknown Title')
            author = doc.get('author_name', ['Unknown Author'])[0] if doc.get('author_name') else 'Unknown Author'
            
            return f"Title: {title}\nAuthor: {author}"
        except requests.RequestException as e:
            return f"Error fetching data: {e}"
        except (KeyError, IndexError) as e:
            return f"Error parsing response: {e}"


# results = Search().get_search_results()
# print(results)

# results_json = Search().get_search_results_json()
# print(json.dumps(results_json, indent=1))

search_term = input("Enter a book title: ")
result = Search().get_user_search_results(search_term)
print("Search Result:\n")
print(result)
