📢 Text-to-Speech Web Application

🔍 Project Description
This project is a Text-to-Speech (TTS) web application built using Python (Flask) and the ElevenLabs Text-to-Speech API. It allows users to enter any text into a web interface and instantly convert it into high-quality, natural-sounding speech.The application provides a clean, user-friendly interface where users can generate audio, listen to it directly in the browser, and download the generated speech as an MP3 file.

🚀 Key Features
1) Convert written text into realistic human-like speech
2) Simple and responsive web interface
3) Audio playback directly in the browser
4) Download generated audio in MP3 format
5) Error handling for empty input and API issues
6) Secure API key management using environment variables

🛠️ Technologies Used
1) Backend: Python, Flask
2) Frontend: HTML, CSS, JavaScript
3) API: ElevenLabs Text-to-Speech API
4) Environment Management: python-dotenv
5) Audio Format: MP3

⚙️ How It Works
1) The user enters text into the input box.
2) The Flask backend sends the text to the ElevenLabs API.
3) The API generates speech audio from the text.
4) The audio file is saved on the server.
5) The user can listen to or download the generated audio.

🎯 Use Cases
1) Accessibility support for visually impaired users
2) Voice narration for content creators
3) Educational tools and e-learning platforms
4) Audiobook and podcast creation
5) Language learning applications

🔐 Security
The ElevenLabs API key is securely stored in a .env file and is never exposed in the frontend code.

📌 Conclusion
This Text-to-Speech application demonstrates how modern AI voice technology can be integrated into a web application to create an intuitive and powerful tool for converting text into speech. The project highlights backend API integration, frontend design, and real-time audio generation.
