# Vocabulary Practice Tool

A comprehensive Python application designed to help students practice spelling and vocabulary through interactive audio-visual learning. The tool uses text-to-speech technology to pronounce words while tracking progress and providing real-time feedback.

## Features

- **Audio-First Learning**: Text-to-speech pronunciation of vocabulary words
- **Multiple Word Lists**: Organized categories including Academic Word Lists (Sublists 1-10), subject-specific vocabulary, and common word groups
- **Progress Tracking**: Real-time statistics showing correct/incorrect answers and remaining words
- **Mistake Tracking**: Visual list of misspelled words for focused review
- **Interactive GUI**: Clean, user-friendly interface built with Tkinter
- **Flexible Input**: Type answers or write on paper (blank entry counts as correct for motivation)
- **Word Definitions**: Enhanced version includes dictionary API integration for word meanings

## Screenshots

The application features a split-screen design:
- **Left Panel**: Word selection, controls, input field, and progress statistics
- **Right Panel**: List of misspelled words for review

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/aafaebeb-ef61-4d8b-8917-f0a8df236377" />
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/d2636d86-17db-499c-a97e-b919a9beb910" />
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/42a95281-005b-488f-af1d-2a1a61a865ff" />
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/3773ff03-ce98-4fad-9f35-1a84f27ceb29" />
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/96f49a57-0fa0-4ee9-825b-b868bb678612" />


## Installation

### Prerequisites

- Python 3.7 or higher
- Required Python packages (install via pip):

```bash
pip install pyttsx3 requests
```

### Setup

1. Clone this repository:
```bash
git clone https://github.com/Afif718/Vocabulary-Practice-Tool.git
cd Vocabulary-Practice-Tool
```

2. Ensure all files are in the same directory:
   - `main.py` (basic version)
   - `vocab_trainer.py` (enhanced version with definitions)
   - `vocab_words.json` (vocabulary database)

3. Run the application:
```bash
# Basic version
python main.py

# Enhanced version with definitions
python vocab_trainer.py
```

## Usage

### Getting Started

1. **Launch the Application**: Run either `main.py` or `vocab_trainer.py`
2. **Select a Word List**: Choose from the dropdown menu (shows word count for each category)
3. **Start Practice**: Click the "▶️ Start" button
4. **Listen & Spell**: The app will pronounce each word - type the spelling or write it on paper
5. **Review Progress**: Monitor your statistics and review misspelled words

### Word Categories

The application includes comprehensive vocabulary lists:

**Academic Lists (570+ words)**
- Sublist 1-10: Academic Word List for higher education and professional contexts

**Themed Categories**
- Time & Dates: Days, months, time expressions
- Money & Finance: Banking, transactions, financial terms
- Education: University, courses, academic terminology
- Nature & Environment: Geography, climate, conservation
- Health & Wellness: Medical terms, nutrition, exercise
- Animals & Plants: Biological classifications and terms
- Travel & Places: Countries, cities, transportation
- Professional: Jobs, workplace vocabulary
- And many more specialized categories

### Controls

- **▶️ Start**: Begin practice session with selected word list
- **⏹️ Stop**: Pause current session
- **Text Input Field**: Type your spelling attempt
- **Statistics Panel**: Shows correct answers, mistakes, and remaining words

### Practice Modes

1. **Type Mode**: Enter spelling in the text field
2. **Paper Mode**: Leave field blank (counts as correct for self-assessment)
3. **Mixed Mode**: Combine both approaches as needed

## File Structure

```
vocabulary-practice-tool/
├── main.py                 # Basic version of the application
├── vocab_trainer.py        # Enhanced version with dictionary API
├── vocab_words.json        # Vocabulary database (JSON format)
├── README.md              # This file
└── screenshots/           # Application screenshots (optional)
```

## Technical Details

### Architecture

- **GUI Framework**: Tkinter (Python standard library)
- **Text-to-Speech**: pyttsx3 library
- **Data Storage**: JSON format for vocabulary lists
- **Threading**: Background audio processing to prevent UI freezing
- **API Integration**: Dictionary API for word definitions (enhanced version)

### Key Components

1. **Vocabulary Management**: JSON-based word list storage with categorization
2. **Audio Engine**: Configurable speech synthesis (rate: 130 WPM)
3. **Progress Tracking**: Real-time statistics and mistake logging
4. **User Interface**: Responsive layout with visual feedback

### Customization

#### Adding New Word Lists

Edit `vocab_words.json` to add new categories:

```json
{
  "Your Custom Category": ["word1", "word2", "word3"],
  "Another Category": ["term1", "term2", "term3"]
}
```

#### Adjusting Speech Settings

Modify the TTS engine properties in the Python files:

```python
engine.setProperty("rate", 130)    # Speech rate (words per minute)
engine.setProperty("voice", voice) # Voice selection
```

## Educational Benefits

### Learning Objectives

- **Spelling Proficiency**: Improve accurate spelling through audio-visual reinforcement
- **Vocabulary Expansion**: Learn new words across academic and professional domains
- **Pronunciation**: Develop proper pronunciation through audio feedback
- **Self-Assessment**: Build confidence through progress tracking
- **Focused Review**: Target problem areas through mistake tracking

### Pedagogical Approach

- **Multi-Sensory Learning**: Combines auditory, visual, and kinesthetic elements
- **Immediate Feedback**: Instant correction and reinforcement
- **Spaced Practice**: Systematic exposure to vocabulary sets
- **Error Analysis**: Identification of patterns in spelling difficulties
- **Motivation Through Progress**: Visual statistics encourage continued practice

## Use Cases

### Academic Settings

- **ESL/EFL Students**: Building English vocabulary and spelling skills
- **Test Preparation**: SAT, GRE, TOEFL, IELTS vocabulary practice
- **University Students**: Academic writing and professional terminology
- **Language Learning**: Supplementary tool for vocabulary acquisition

### Professional Development

- **Business English**: Professional vocabulary for workplace communication
- **Technical Fields**: Specialized terminology for various industries
- **Writing Skills**: Improving written communication accuracy

### Personal Learning

- **Self-Study**: Independent vocabulary building
- **Homeschooling**: Educational tool for spelling and vocabulary
- **Adult Education**: Continuing education and skill development

## Contributing

We welcome contributions to improve the Vocabulary Practice Tool:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

### Contribution Ideas

- Additional word lists and categories
- UI/UX improvements
- Performance optimizations
- New features (difficulty levels, timed modes, etc.)
- Bug fixes and error handling improvements

## Troubleshooting

### Common Issues

**TTS Not Working**
- Ensure pyttsx3 is installed: `pip install pyttsx3`
- Check system audio settings
- Try different voice engines (platform-specific)

**JSON File Errors**
- Verify `vocab_words.json` is in the same directory
- Check JSON syntax validity
- Ensure proper UTF-8 encoding

**Performance Issues**
- Close other audio applications
- Restart the application
- Check system resources

## Requirements

Create a `requirements.txt` file:

```
pyttsx3>=2.90
requests>=2.25.1
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Academic Word List based on Coxhead's Academic Word List
- Dictionary definitions provided by Free Dictionary API
- Text-to-speech functionality powered by pyttsx3

## Version History

- **v1.0**: Basic vocabulary practice with TTS
- **v1.1**: Added progress tracking and mistake logging
- **v2.0**: Enhanced version with dictionary API integration

---

**Happy Learning!** 📚✨

For questions, suggestions, or support, please open an issue on GitHub or contact the maintainer.
