# CHAT_BOT

### It is created by uing API-KEY which is OpenAI - API

This repository contains a simple chatbot application built using Flask and OpenAI's GPT-3.5-turbo model. The chatbot allows users to interact with an AI assistant through a web interface.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/sameerraj-13/CHAT_BOT.git
    cd CHAT_BOT
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate    # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set your OpenAI API key:**
    Replace `"API_KEY"` in `app.py` with your actual OpenAI API key.

## Usage

1. **Run the Flask application:**
    ```bash
    python app.py
    ```

2. **Open your web browser and go to:**
    ```
    http://127.0.0.1:5000/
    ```

3. **Interact with the chatbot:**
    Type your message in the input box and click "Send". The chatbot will respond to your message.

## Features

- **AI-Powered Chatbot:** Uses OpenAI's GPT-3.5-turbo model to generate responses.
- **Web Interface:** Simple and intuitive web interface built with HTML, CSS, and JavaScript.
- **Flask Backend:** Lightweight backend using Flask to handle requests and responses.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
