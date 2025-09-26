# TaskOptimus

An open-source, AI-powered task prioritizer to optimize your daily workflow. Input tasks with urgency and importance scores, and TaskOptimus will suggest the best order to tackle them. Built with extensibility in mind for future AI enhancements and integrations.

## Features
- Add tasks with custom urgency (1-10) and importance (1-10) scores.
- Prioritize tasks using a weighted scoring algorithm (60% urgency, 40% importance).
- Simple command-line interface (CLI) for easy interaction.
- Modular design for scalability (e.g., add ML models, web UI, or API integrations).

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/OptioOpusSecundus/TaskOptimus.git
   ```
2. Navigate to the project directory:
   ```bash
   cd TaskOptimus
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Usage
1. Launch the app with `python main.py`.
2. Choose options:
   - **Add Task**: Enter task name, urgency (1-10), and importance (1-10).
   - **View Prioritized Tasks**: See tasks sorted by priority score.
   - **Exit**: Close the application.

## Contributing
We welcome contributions! Please:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## Future Enhancements
- Integrate machine learning models (e.g., scikit-learn) for smarter prioritization.
- Add a web interface using Flask or FastAPI.
- Support task storage with SQLite or other databases.
- Integrate with Google Calendar or other productivity APIs.

## License
MIT License - feel free to use, modify, and distribute.