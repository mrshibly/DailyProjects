import requests
from bs4 import BeautifulSoup
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import readability
import argparse
from tabulate import tabulate

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

class URLAnalyzer:
    def __init__(self, url):
        self.url = url
        self.html_content = self.fetch_webpage()
        self.soup = BeautifulSoup(self.html_content, 'html.parser')

    def fetch_webpage(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the webpage: {e}")
            exit()

    def get_title(self):
        return self.soup.title.string if self.soup.title else 'No title found'

    def get_meta_description(self):
        description = self.soup.find('meta', attrs={'name': 'description'})
        return description['content'] if description else 'No description found'

    def get_all_links(self):
        links = [a['href'] for a in self.soup.find_all('a', href=True)]
        return links

    def get_text_content(self):
        for script in self.soup(["script", "style"]):
            script.extract()
        text = self.soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        return text

    def analyze_text(self, text):
        tokens = word_tokenize(text)
        words = [word for word in tokens if word.isalpha()]
        stop_words = set(stopwords.words('english'))
        filtered_words = [word for word in words if word.lower() not in stop_words]
        word_freq = Counter(filtered_words)
        return word_freq

    def get_readability_scores(self, text):
        results = readability.getmeasures(text, lang='en')
        return results['readability grades']

    def analyze_url(self, analyze_links, analyze_text):
        title = self.get_title()
        description = self.get_meta_description()
        analysis_results = {
            'Title': title,
            'Description': description
        }

        if analyze_links:
            links = self.get_all_links()
            analysis_results['Number of Links'] = len(links)
            analysis_results['Links'] = links

        if analyze_text:
            text_content = self.get_text_content()
            word_freq = self.analyze_text(text_content)
            readability_scores = self.get_readability_scores(text_content)
            analysis_results['Word Frequency'] = word_freq
            analysis_results['Readability Scores'] = readability_scores

        return analysis_results

def main():
    parser = argparse.ArgumentParser(description="Analyze a web URL",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('url', type=str, help='The URL to analyze')
    parser.add_argument('--links', action='store_true', help='Include link analysis')
    parser.add_argument('--text', action='store_true', help='Include text content analysis')
    args = parser.parse_args()

    analyzer = URLAnalyzer(args.url)
    results = analyzer.analyze_url(args.links, args.text)

    for key, value in results.items():
        if isinstance(value, dict):
            print(f"\n{key}:\n{tabulate(value.items(), headers=['Metric', 'Value'])}")
        elif isinstance(value, list):
            print(f"\n{key}:")
            for item in value:
                print(f"- {item}")
        else:
            print(f"{key}: {value}")

if __name__ == '__main__':
    main()
