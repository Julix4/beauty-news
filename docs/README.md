# Beauty News AI - Process Summary Structure

## 🔄 Complete Process Flow

### 1. **INITIALIZATION PHASE**
```
📁 Configuration Setup
├── Load environment variables (.env)
├── Import keywords from data/keywords.py
├── Set API keys (GOOGLE_API_KEY, GEMINI_API_KEY)
└── Define preferred sources list
```

### 2. **NEWS FETCHING PHASE**
```
🔍 News Discovery
├── Input: Keywords + Preferred Sources + API Key
├── API Call: SerpAPI Google News Search
│   ├── Engine: google_news
│   ├── Query: Keywords joined with "OR"
│   ├── Filters: English, recent (daily), specific countries
│   └── Device: desktop
├── Response Processing
│   ├── Extract news_results from JSON
│   ├── Error handling (status code check)
│   └── Return raw news data
└── Output: Raw news articles array
```

### 3. **SCORING & FILTERING PHASE**
```
⚖️ Article Evaluation
├── Input: Raw news articles
├── Scoring Algorithm
│   ├── Check source URL against preferred sources
│   ├── Calculate priority score (source match * 10)
│   └── Keyword relevance check in title
├── Article Structure Creation
│   ├── title
│   ├── link
│   ├── source
│   ├── published date
│   └── calculated score
├── Filtering: Keep only keyword-relevant articles
├── Sorting: By score (highest first)
└── Output: Top N scored articles (default: 6)
```

### 4. **CONTENT SCRAPING PHASE** *(separate script)*
```
📰 Article Content Extraction
├── Input: Article URLs from previous phase
├── Web Scraping Process
│   ├── Send HTTP requests to article URLs
│   ├── Parse HTML content
│   ├── Extract main article text
│   └── Clean and format content
└── Output: Full article content for each URL
```

### 5. **AI SUMMARIZATION PHASE** *(separate script)*
```
🤖 Content Processing
├── Input: Scraped article content + Platform specs
├── Gemini AI Configuration
│   ├── Model: gemini-2.0-flash-exp
│   ├── Temperature: 1
│   ├── Max tokens: 8192
│   └── Platform-specific instructions
├── Content Generation
│   ├── Analyze multiple articles
│   ├── Extract key insights
│   ├── Create platform-optimized content
│   └── Apply length and style requirements
└── Output: Ready-to-publish article drafts
```

## 🏗️ System Architecture

### **Data Flow**
```
Environment Setup → Keywords Loading → News Fetching → Scoring → Filtering → Scraping → AI Processing → Publication
```

### **Key Components**

#### **Input Sources**
- **Keywords Dictionary**: `data/keywords.py`
  - News keywords: beauty trends, skincare, makeup, cosmetics, beauty tech, acne remedies
  - Scholar keywords: cosmetic science, skincare, beauty technology, anti-aging, nutraceuticals

- **Preferred Sources**: High-priority beauty publications
  - theindustry.beauty, businessoffashion.com, glossy.co
  - whowhatwear.com, allure.com, vogue.com, marieclaire.com
  - And more specialized beauty/fashion sources

#### **API Dependencies**
- **SerpAPI**: Google News search functionality
- **Gemini AI**: Content summarization and article generation
- **Environment Variables**: Secure API key management

#### **Output Formats**
- **Scored Articles**: JSON structure with metadata
- **Article Content**: Scraped full-text content
- **Generated Articles**: Platform-specific formatted content

## 📊 Process Metrics

### **Filtering Criteria**
- **Geographic**: GB, US, AU, CA countries
- **Language**: English only
- **Recency**: Daily articles (last 24 hours)
- **Relevance**: Keyword match in article title
- **Quality**: Source prioritization scoring

### **Scoring Algorithm**
```python
priority_score = sum(preferred_source in article_url for preferred_source in sources)
final_score = priority_score * 10
```

### **Default Parameters**
- **Articles returned**: 6 per query
- **Search scope**: Daily news
- **Language**: English
- **Target regions**: English-speaking countries

## 🔧 Configuration Points

### **Customizable Elements**
1. **Keywords**: Modify `data/keywords.py` for different focus areas
2. **Source Priority**: Update PREFERRED_SOURCES list
3. **Article Count**: Adjust `num_articles` parameter
4. **Geographic Scope**: Modify country filters
5. **Time Range**: Change `tbs` parameter for different periods
6. **AI Model**: Configure Gemini model parameters

### **Environment Variables Required**
```
GOOGLE_API_KEY=your_serpapi_key
GEMINI_API_KEY=your_gemini_api_key
```

## 🚀 Execution Flow

1. **Manual Execution**: Run individual scripts
2. **Article creation**: Use `create_articles.py` for article creation
3. **Batch Processing**: Use `run_all.py` for complete pipeline
4. **Platform-Specific**: Separate Medium/Substack workflows
5. **Scheduling**: Cron jobs for automated execution

This structure provides a comprehensive overview suitable for creating process diagrams, system documentation, or workflow automation.
