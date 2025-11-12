# ✈️ AI Travel Planner

An intelligent travel planning assistant powered by AI that creates comprehensive, personalized travel itineraries. Built with LangGraph, FastAPI, and Streamlit, this agentic system uses multiple tools to provide real-time travel recommendations including weather forecasts, place information, budget calculations, and currency conversions.

![Python Version](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 🌟 Features

- **🤖 Agentic Workflow**: Utilizes LangGraph for intelligent decision-making and tool orchestration
- **🗺️ Custom Itineraries**: Day-by-day travel plans tailored to your preferences
- **🏨 Hotel Recommendations**: Best accommodation options with approximate costs
- **🍽️ Restaurant Suggestions**: Local cuisine hotspots with pricing information
- **💰 Budget Planning**: Detailed cost breakdowns and daily expense estimates
- **🌤️ Weather Forecasts**: Real-time weather information for your destination
- **💱 Currency Conversion**: Automatic currency calculations for international travel
- **🚗 Transportation Info**: Best travel modes and transportation options
- **🎯 Dual Plans**: Generic tourist attractions + off-beat hidden gems

## 🏗️ Architecture

The application uses an agentic workflow built with LangGraph that orchestrates multiple specialized tools:

```
User Query → FastAPI Backend → LangGraph Agent → Tools → AI Response
                                      ↓
                    ┌─────────────────┼─────────────────┐
                    ↓                 ↓                 ↓
            Weather Tools      Place Search      Calculator
            Currency Conv.     Tavily Search     Cost Estimator
```

## 🛠️ Tech Stack

- **Backend Framework**: FastAPI
- **Frontend**: Streamlit
- **AI Orchestration**: LangGraph
- **LLM**: Groq (DeepSeek R1 Distill Llama 70B)
- **Search**: Tavily API
- **Weather**: OpenWeatherMap API
- **Currency**: Exchange Rate API
- **Deployment**: Render

## 📋 Prerequisites

- Python 3.11+
- API Keys:
  - Groq API Key
  - Tavily API Key
  - OpenWeatherMap API Key
  - Exchange Rate API Key

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/AI_Travel_Planner.git
cd AI_Travel_Planner
```

### 2. Set Up Virtual Environment

Using UV (recommended):

```bash
# Install UV
pip install uv

# Create virtual environment
uv venv env --python cpython-3.10.18-windows-x86_64-none

# Activate virtual environment
# On Windows
.\env\Scripts\activate
# On macOS/Linux
source env/bin/activate
```

Using standard Python:

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or with UV:

```bash
uv pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
OPENWEATHERMAP_API_KEY=your_openweather_api_key_here
EXCHANGE_RATE_API_KEY=your_exchange_rate_api_key_here
```

## 🎮 Usage

### Running the Backend (FastAPI)

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### Running the Frontend (Streamlit)

```bash
streamlit run app.py
```

The web interface will open at `http://localhost:8501`

### API Endpoints

#### POST `/query`

Submit a travel planning query.

**Request Body:**
```json
{
  "question": "Plan a 5-day romantic trip to Paris with a budget of $2000 for 2 people"
}
```

**Response:**
```json
{
  "answer": "# 🌍 Your Paris Travel Plan\n\n## Day 1: Arrival...\n\n..."
}
```

## 📝 Example Queries

- "Plan a 7-day adventure trip to New York City"
- "Budget-friendly 3-day weekend in Barcelona"
- "Family vacation to Tokyo for 5 days with kids"
- "Romantic honeymoon in Maldives for a week"
- "Solo backpacking trip across Thailand"

## 🔧 Project Structure

```
AI_Travel_Planner/
├── agent/
│   ├── __init__.py
│   └── agentic_workflow.py      # LangGraph agent implementation
├── tools/
│   ├── __init__.py
│   ├── weather_info_tool.py     # Weather forecasting tools
│   ├── place_search_tool.py     # Place search and info tools
│   ├── calculator_tool.py       # Cost calculation tools
│   └── currency_conversion_tool.py
├── utils/
│   ├── __init__.py
│   ├── model_loader.py          # LLM configuration
│   ├── weather_info.py          # Weather API wrapper
│   ├── place_info_search.py     # Tavily search wrapper
│   ├── calculator.py            # Budget calculations
│   └── currency_converter.py    # Currency conversion logic
├── prompt_library/
│   ├── __init__.py
│   └── prompt.py                # System prompts
├── config/
│   ├── __init__.py
│   └── config.yaml              # Configuration settings
├── main.py                      # FastAPI application
├── app.py                       # Streamlit frontend
├── requirements.txt
├── setup.py
└── README.md
```

## 🧰 Tools & Capabilities

### Weather Tools
- **get_current_weather**: Real-time weather conditions
- **get_weather_forecast**: 5-day weather predictions

### Place Search Tools
- **search_attractions**: Top tourist attractions and landmarks
- **search_restaurants**: Local dining recommendations
- **search_activities**: Things to do and experiences
- **search_transportation**: Available transport modes

### Calculator Tools
- **estimate_total_hotel_cost**: Calculate accommodation expenses
- **calculate_total_expense**: Sum up all trip costs
- **calculate_daily_expense_budget**: Per-day budget breakdown

### Currency Tools
- **convert_currency**: Real-time currency conversion

## 🎨 Features in Detail

### Intelligent Itinerary Generation
The AI agent creates comprehensive travel plans that include:
- Detailed day-by-day schedules
- Time-optimized activity sequences
- Budget-friendly alternatives
- Off-beat locations for authentic experiences

### Real-Time Data Integration
- Live weather forecasts
- Current currency exchange rates
- Up-to-date place information
- Recent travel recommendations

### Markdown Export
Download your complete travel plan as a formatted Markdown file for offline reference.

## 🌐 Deployment

The application is deployed on Render:
- Backend: `https://agentic-trip-planner-gbfn.onrender.com/`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Navodit Sahai**
- Email: sahainavodit781@gmail.com
- GitHub: [@yourusername](https://github.com/yourusername)

## 🙏 Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain) for the amazing framework
- [LangGraph](https://github.com/langchain-ai/langgraph) for agentic workflows
- [Groq](https://groq.com/) for lightning-fast LLM inference
- [Tavily](https://tavily.com/) for web search capabilities
- [OpenWeatherMap](https://openweathermap.org/) for weather data
- [Streamlit](https://streamlit.io/) for the beautiful UI framework

## 📞 Support

For support, email sahainavodit781@gmail.com or open an issue in the repository.

## 🗺️ Roadmap

- [ ] Multi-language support
- [ ] Flight booking integration
- [ ] Hotel booking integration
- [ ] Interactive map visualization
- [ ] User authentication and saved itineraries
- [ ] Mobile application
- [ ] Collaborative trip planning
- [ ] Social sharing features

---

⭐ If you found this project helpful, please consider giving it a star on GitHub!

**Happy Traveling! ✈️🌍**
