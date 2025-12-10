# 0x16. API Advanced

## 📚 Project Overview

This project explores advanced API interaction concepts using the **Reddit API**. Through a series of progressively complex tasks, you'll learn how to query APIs, parse JSON responses, handle pagination, and implement recursive functions—all essential skills for working with RESTful APIs in real-world applications.

The project demonstrates practical API concepts including authentication, endpoint navigation, recursive data retrieval, and data processing with external APIs.

---

## 🎯 Learning Objectives

By completing this project, you will understand:

- How to read and navigate API documentation to find relevant endpoints
- How to use pagination to retrieve large datasets from APIs
- How to parse and process JSON data from API responses
- How to make recursive API calls for comprehensive data collection
- How to sort and manipulate dictionaries in Python
- How to handle API rate limits and errors gracefully

---

## 🛠️ Technology Stack

- **Language**: Python 3
- **API**: Reddit API (https://www.reddit.com/dev/api/)
- **Libraries**: 
  - `requests` - For making HTTP requests
  - `json` - For parsing JSON responses
  - `sys` - For command-line arguments

---

## 📋 Project Structure

```
0x16-api_advanced/
├── 0-subs.py           # Get subscriber count for a subreddit
├── 1-top_ten.py        # Display top 10 hot posts
├── 2-recurse.py        # Recursively get all hot articles
├── 100-count.py        # Count and sort keywords in hot articles
├── README.md           # Project documentation
└── __pycache__/        # Python cache directory
```

---

## 📝 Task Descriptions

### Task 0: How Many Subscribers? (`0-subs.py`)

**Function**: `number_of_subscribers(subreddit)`

Queries the Reddit API and returns the number of subscribers for a given subreddit. If the subreddit is invalid, the function returns `0`.

**Usage**:
```python
import 0-subs

subscribers = number_of_subscribers("python")
print(subscribers)  # Output: Number of subscribers
```

**Key Concepts**:
- Basic API GET requests
- JSON response parsing
- Error handling for invalid subreddits

---

### Task 1: Top Ten (`1-top_ten.py`)

**Function**: `top_ten(subreddit)`

Prints the titles of the first 10 hot posts for a given subreddit. If the subreddit is invalid, it prints `None`.

**Usage**:
```python
import 1-top_ten

top_ten("python")
# Output: Prints titles of top 10 hot posts
```

**Key Concepts**:
- Querying specific API endpoints
- Limiting results using query parameters
- Iterating through JSON arrays

---

### Task 2: Recurse It! (`2-recurse.py`)

**Function**: `recurse(subreddit, hot_list=[])`

Recursively queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. Returns `None` if the subreddit is invalid.

**Usage**:
```python
import 2-recurse

hot_articles = recurse("python")
print(len(hot_articles))  # Total number of hot articles
```

**Key Concepts**:
- Recursive function implementation
- API pagination using `after` parameter
- Building cumulative results across multiple API calls

---

### Task 3: Count It! (`100-count.py`)

**Function**: `count_words(subreddit, word_list)`

Parses the titles of all hot articles in a subreddit and prints a sorted count of given keywords. Results are sorted first by count (descending), then alphabetically (ascending) for ties.

**Usage**:
```python
import 100-count

word_list = ["python", "java", "javascript"]
count_words("programming", word_list)
# Output: 
# python: 45
# javascript: 30
# java: 15
```

**Key Concepts**:
- Recursive API calls combined with data processing
- Case-insensitive keyword matching
- Dictionary sorting with multiple criteria
- Data aggregation and analysis

---

## 🚀 Installation & Setup

### Prerequisites

- Python 3.4 or higher
- `pip` package manager

### Install Required Libraries

```bash
pip install requests
```

### Set Up User Agent

The Reddit API requires a custom User-Agent header. Make sure to include one in your requests:

```python
headers = {'User-Agent': 'YourCustomUserAgent/1.0'}
```

---

## 💻 Usage Examples

### Example 1: Check Subscriber Count

```bash
python3 -c "
import 0-subs
print(0-subs.number_of_subscribers('python'))
"
```

### Example 2: Get Top 10 Posts

```bash
python3 -c "
import 1-top_ten
top_ten('programming')
"
```

### Example 3: Recursively Get All Hot Posts

```bash
python3 -c "
import 2-recurse
articles = recurse('machinelearning')
print(f'Found {len(articles)} hot articles')
"
```

### Example 4: Count Keywords

```bash
python3 -c "
import 100-count
count_words('python', ['python', 'beginner', 'tutorial'])
"
```

---

## 🔒 API Best Practices

### Rate Limiting

The Reddit API has rate limits. To avoid being blocked:

- Don't make requests too rapidly
- Implement exponential backoff for retries
- Cache results when possible

### User-Agent

Always use a descriptive User-Agent string:

```python
headers = {
    'User-Agent': 'linux:api.advanced.project:v1.0 (by /u/yourusername)'
}
```

### Error Handling

Always check for:
- Invalid subreddit names (404 errors)
- Rate limit exceeded (429 errors)
- Network connectivity issues
- Malformed JSON responses

---

## 📖 Reddit API Endpoints Used

| Endpoint | Purpose |
|----------|---------|
| `/r/{subreddit}/about.json` | Get subreddit information (subscriber count) |
| `/r/{subreddit}/hot.json` | Get hot posts from a subreddit |

**Query Parameters**:
- `limit`: Number of posts to retrieve (max 100 per request)
- `after`: Pagination token for next page of results

---

## 🧪 Testing

To test your functions:

1. **Test with valid subreddits**: `python`, `programming`, `learnpython`
2. **Test with invalid subreddits**: `this_is_not_a_real_subreddit_xyz`
3. **Test edge cases**: Empty subreddits, very large subreddits
4. **Test pagination**: Subreddits with 100+ hot posts

---

## ⚠️ Common Pitfalls

1. **Not handling redirects**: Some subreddit names redirect (e.g., old names)
2. **Case sensitivity**: Subreddit names are case-insensitive, but keywords might not be
3. **Infinite recursion**: Always check if `after` is `None` to prevent infinite loops
4. **Missing User-Agent**: Requests without User-Agent may be blocked
5. **Not following API guidelines**: Read Reddit's API rules and rate limits

---

## 📚 Resources

- [Reddit API Documentation](https://www.reddit.com/dev/api/)
- [Python Requests Library](https://docs.python-requests.org/)
- [Recursive Functions in Python](https://realpython.com/python-recursion/)
- [JSON Parsing in Python](https://docs.python.org/3/library/json.html)

---

## 🤝 Contributing

If you'd like to improve this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

## 📄 License

This project is part of a programming curriculum and is intended for educational purposes.

---

## ✨ Acknowledgments

- Reddit for providing a free, accessible API
- The Python community for excellent documentation and libraries
- All contributors who help improve API interaction patterns

---

## 🎓 Author

Project completed as part of advanced API interaction training.

---

*Happy API Hacking! 🚀*
