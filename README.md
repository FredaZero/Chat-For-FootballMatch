# Chat-For-FootballMatch ⚽💬

**Chat-For-FootballMatch** is a Rasa-based conversational AI chatbot that allows users to query football match records through natural language. The bot understands user intents, extracts entities, and provides match-related responses based on predefined training data and rules.


<img width="739" alt="截屏2025-06-24 20 15 22" src="https://github.com/user-attachments/assets/c5a9fb6c-440e-4a60-9a9b-916d02944fcb" />

---

## 🚀 Features

- Natural language interaction for football match queries
- Custom intent classification and entity extraction
- Rule-based dialogue flows using Rasa Stories and Rules
- Integration-ready via command line or web chat

---

## 📦 Requirements

- Python 3.8 or higher recommended
- Rasa (install via pip)
- Optional: virtual environment (`venv` or `conda`) for dependency isolation

Install Rasa:

```bash
pip install rasa
```

Install other dependencies:

```bash
pip install -r requirements.txt
```

---

## 📁 Project Structure
```bash
.
├── data/                 # NLU training data and dialogue flows
│   ├── nlu.yml
│   ├── rules.yml
│   └── stories.yml
├── domain.yml            # Domain definition (intents, entities, slots, responses, etc.)
├── actions/              # Custom actions logic
│   └── actions.py
├── config.yml            # NLU pipeline and policy configuration
├── credentials.yml       # Channel credentials
├── endpoints.yml         # Server endpoints
├── football_match_check.mov  # Demo video
└── README.md             # You're reading it!
```
---

## 🛠️ How to Use
**Train the Rasa model**
Run the following to train the model using your NLU data, rules, and stories:
```bash
rasa train
```
**Start Rasa HTTP server**
This enables integration with external interfaces:
```bash
rasa run
```

---

## 🧠 Customization Ideas

You can extend the bot by:

- Adding more intents and training examples
- Defining new slots and entities
- Creating more dialogue paths and stories

