# SQL Database Chatbot 🗄️

A professional Streamlit application that enables natural language querying of SQL databases using LangChain and Large Language Models. Chat with your databases using plain English and get instant SQL query results.

## Features

- **Natural Language Queries**: Ask questions in plain English and get SQL results
- **Multiple Database Support**: Works with SQLite and MySQL databases
- **Real-time Streaming**: Get responses as they're generated
- **Professional UI**: Clean, intuitive interface built with Streamlit
- **Secure Connections**: Environment variable support for API keys
- **Error Handling**: Robust error management and user feedback

## Demo

![SQL Database Chatbot Demo](https://via.placeholder.com/800x400?text=SQL+Database+Chatbot+Demo)

## Prerequisites

- Python 3.8 or higher
- Groq API key (for LLM access)
- Database files (SQLite) or MySQL server access

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AdeelIntizar/SQL-Database-Chatbot.git
cd SQL-Database-Chatbot
```

### 2. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root (optional but recommended):

```bash
GROQ_API_KEY=your_groq_api_key_here
```

Alternatively, you can set the API key directly in the code or use the default embedded key for testing.

## Usage

### Running the Application

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

### Database Setup

#### SQLite (Default)
- Place your SQLite database file named `student.db` in the project directory
- The app will automatically detect and connect to it

#### MySQL
1. Select "MySQL Database (Remote)" in the sidebar
2. Fill in your MySQL connection details:
   - Host (e.g., localhost)
   - Username
   - Password
   - Database name
3. Click "Connect to MySQL"

### Example Queries

Once connected, you can ask questions like:

- "Show me all students"
- "What is the average grade?"
- "How many students are in each department?"
- "Find students with grades above 85"
- "Show the top 5 performing students"

## Project Structure

```
SQL-Database-Chatbot/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── student.db            # Sample SQLite database (optional)
├── README.md             # Project documentation
└── .env                  # Environment variables (create this)
```

## Dependencies

### Core Requirements
```
streamlit
langchain
langchain-groq
sqlalchemy
mysql-connector-python
```

### Full Requirements (requirements.txt)
```
streamlit==1.28.1
langchain==0.0.350
langchain-groq==0.0.1
sqlalchemy==2.0.23
mysql-connector-python==8.2.0
pathlib
sqlite3
```

## Configuration

### Environment Variables
- `GROQ_API_KEY`: Your Groq API key for LLM access

### Database Types Supported
- **SQLite**: Local database files
- **MySQL**: Remote MySQL servers

## API Keys

### Getting a Groq API Key
1. Visit [Groq Console](https://console.groq.com/)
2. Sign up for a free account
3. Generate an API key
4. Add it to your `.env` file or use it directly in the app

## Troubleshooting

### Common Issues

**Database Connection Error**
- Ensure your database file exists (for SQLite)
- Verify MySQL connection details are correct
- Check network connectivity for remote databases

**API Key Error**
- Verify your Groq API key is valid
- Check if you have sufficient API credits

**Import Errors**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Try creating a fresh virtual environment

**Streamlit Not Found**
- Make sure Streamlit is installed: `pip install streamlit`
- Verify you're using the correct Python environment

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Adeel Intizar**
- GitHub: [@AdeelIntizar](https://github.com/AdeelIntizar)
- LinkedIn: [Connect with me](https://linkedin.com/in/your-profile)

## Acknowledgments

- [LangChain](https://python.langchain.com/) for the SQL agent framework
- [Streamlit](https://streamlit.io/) for the web interface
- [Groq](https://groq.com/) for fast LLM inference

## Support

If you find this project helpful, please give it a ⭐ on GitHub!

For issues and questions, please open an issue in the [GitHub repository](https://github.com/AdeelIntizar/SQL-Database-Chatbot/issues).

---

*Built with ❤️ using Python, Streamlit, and LangChain*