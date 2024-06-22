# URLAnalyzer

URLAnalyzer is a Python tool for analyzing various aspects of a web URL. It fetches the webpage content, extracts metadata (like title and description), analyzes links, and performs text content analysis including word frequency and readability scores.

## Features

- **Fetch Webpage Content**: Retrieve HTML content from a specified URL.
- **Extract Metadata**: Get the page title and meta description.
- **Link Analysis**: Optional feature to analyze all links present on the webpage.
- **Text Content Analysis**: Optional feature to analyze text content for word frequency and readability scores.
- **User-friendly Command-line Interface**: Easy to use with command-line arguments for customization.

## Usage

### Installation

1. Clone the repository or download the `url_analyzer.py` file.

2. Install dependencies:
   ```bash
   pip install requests beautifulsoup4 nltk readability-lxml tabulate
   ```

### Basic Usage

To analyze a webpage and display the title and meta description:
```bash
python url_analyzer.py https://www.example.com
```

### Advanced Usage

To include link analysis:
```bash
python url_analyzer.py https://www.example.com --links
```

To include text content analysis:
```bash
python url_analyzer.py https://www.example.com --text
```

To include both link and text content analysis:
```bash
python url_analyzer.py https://www.example.com --links --text
```

## Contributing

Contributions are welcome! Feel free to submit issues or propose new features.
