# Auto-Site-Visitor
# Auto-Site-Visitor

Auto-Site-Visitor is a Python automation script that allows users to visit a given URL using free proxies. It mimics human-like behavior by scrolling through the page and introduces random delays to avoid spamming. The script fetches proxies from multiple sources, tests them for compatibility, and utilizes valid ones to access the target site.

## Features

- Fetches free proxies from multiple reliable sources:
  - [free-proxy-list.net](https://free-proxy-list.net)
  - [spys.me](https://spys.me)
- Tests proxies to ensure they are functional and support HTTPS.
- Visits a user-specified URL using working proxies.
- Simulates human-like scrolling with random delays.
- Avoids spamming by introducing a time delay between visits.

## Requirements

### Prerequisites
- **Python 3.8+**
- **Google Chrome** (latest version)
- **ChromeDriver** (compatible with your Chrome version)

### Python Libraries
Install the required libraries using pip:
``bash
pip install selenium requests

git clone https://github.com/imuhsinalishah/Auto-Site-Visitor.git
cd Auto-Site-Visitor


Fetching proxies from free-proxy-list.net...
Proxy 200.24.141.161:999 failed.
Proxy 37.143.129.242:47224 is working.
Visiting https://example.com using proxy 37.143.129.242:47224
Completed scrolling with proxy 37.143.129.242.


Auto-Site-Visitor/
├── main.py              # Main script to run the tool
├── README.md            # Project documentation
└── requirements.txt     # Optional: Dependencies for easy setup



