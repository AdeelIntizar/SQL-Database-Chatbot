
import streamlit as st
from pathlib import Path
from typing import Optional
import sqlite3
import os
from sqlalchemy import create_engine
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain_groq import ChatGroq


# Configuration Constants
class DatabaseType:
    SQLITE = "sqlite"
    MYSQL = "mysql"

class Config:
    PAGE_TITLE = "SQL Database Chat Interface"
    PAGE_ICON = "🗄️"
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    DEFAULT_MODEL = "Llama3-8b-8192"
    SQLITE_DB_NAME = "student.db"
    CACHE_TTL = "2h"


def initialize_page():

    st.set_page_config(
        page_title=Config.PAGE_TITLE,
        page_icon=Config.PAGE_ICON,
        layout="wide"
    )
    st.title("SQL Database Chat Interface")
    st.markdown("*Query your databases using natural language*")


def setup_sidebar() -> tuple[str, dict]:
    """Configure sidebar for database selection and connection parameters."""
    st.sidebar.header("Database Configuration")
    
    database_options = [
        "SQLite Database (Local)",
        "MySQL Database (Remote)"
    ]
    
    selected_option = st.sidebar.radio(
        "Select Database Type:",
        options=database_options,
        help="Choose between local SQLite or remote MySQL database"
    )
    
    db_config = {}
    
    if "MySQL" in selected_option:
        db_type = DatabaseType.MYSQL
        with st.sidebar.form("mysql_config"):
            st.subheader("MySQL Connection Details")
            db_config = {
                "host": st.text_input("Host", placeholder="localhost"),
                "user": st.text_input("Username", placeholder="root"),
                "password": st.text_input("Password", type="password"),
                "database": st.text_input("Database Name", placeholder="mydb")
            }
            submitted = st.form_submit_button("Connect to MySQL")
            
            if submitted and not all(db_config.values()):
                st.error("Please fill in all MySQL connection details.")
                st.stop()
    else:
        db_type = DatabaseType.SQLITE
        st.sidebar.info(f"Using local SQLite database: {Config.SQLITE_DB_NAME}")
    
    return db_type, db_config


@st.cache_resource(ttl=Config.CACHE_TTL)
def initialize_database(db_type: str, config: dict) -> SQLDatabase:

    try:
        if db_type == DatabaseType.SQLITE:
            db_path = Path(__file__).parent / Config.SQLITE_DB_NAME
            if not db_path.exists():
                st.error(f"SQLite database file '{Config.SQLITE_DB_NAME}' not found.")
                st.stop()
            
            creator = lambda: sqlite3.connect(
                f"file:{db_path.absolute()}?mode=ro", 
                uri=True
            )
            engine = create_engine("sqlite:///", creator=creator)
            
        elif db_type == DatabaseType.MYSQL:
            connection_string = (
                f"mysql+mysqlconnector://{config['user']}:{config['password']}"
                f"@{config['host']}/{config['database']}"
            )
            engine = create_engine(connection_string)
        
        return SQLDatabase(engine)
        
    except Exception as e:
        st.error(f"Database connection failed: {str(e)}")
        st.stop()


def initialize_llm() -> ChatGroq:

    return ChatGroq(
        api_key=Config.GROQ_API_KEY,
        model_name=Config.DEFAULT_MODEL,
        streaming=True,
        temperature=0
    )


def create_sql_chat_agent(database: SQLDatabase, llm: ChatGroq):

    toolkit = SQLDatabaseToolkit(db=database, llm=llm)
    
    return create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True
    )


def initialize_chat_history():

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hello! I'm your SQL database assistant. Ask me anything about your data and I'll help you query it using natural language."
            }
        ]


def display_chat_history():

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])


def handle_user_query(agent, user_input: str):


    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    with st.chat_message("assistant"):
        try:
            callback_handler = StreamlitCallbackHandler(st.container())
            response = agent.run(user_input, callbacks=[callback_handler])
            
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.write(response)
            
        except Exception as e:
            error_message = f"Error processing query: {str(e)}"
            st.error(error_message)
            st.session_state.messages.append({"role": "assistant", "content": error_message})


def main():

    initialize_page()

    db_type, db_config = setup_sidebar()

    if st.sidebar.button(" Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

    database = initialize_database(db_type, db_config)

    llm = initialize_llm()
    agent = create_sql_chat_agent(database, llm)

    initialize_chat_history()
    display_chat_history()
    
    user_query = st.chat_input(
        placeholder="Ask questions about your database (e.g., 'Show me all students' or 'What is the average grade?')"
    )
    
    if user_query:
        handle_user_query(agent, user_query)


if __name__ == "__main__":
    main()