# First Automation Project 🚀

A comprehensive web automation testing framework built with Python, Selenium, and PyTest. This project demonstrates automated testing of login functionality using the Page Object Model design pattern.

## 📋 Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Running Tests](#running-tests)
- [Test Reports](#test-reports)
- [Contributing](#contributing)

## ✨ Features

- **Automated Web Testing** with Selenium WebDriver
- **Page Object Model** design pattern implementation
- **Cross-browser Testing** support (Chrome, Firefox)
- **Parallel Test Execution** capability
- **HTML Test Reports** generation
- **Parameterized Testing** with PyTest
- **Robust Element Waiting** strategies
- **Screenshot Capture** on test failures
- **CI/CD Ready** configuration

## 🛠 Technologies Used

- **Python 3.8+**
- **Selenium WebDriver 4.x**
- **PyTest** - Testing framework
- **WebDriver Manager** - Automatic driver management
- **IntelliJ IDEA** - Development environment

## 📁 Project Structure

```
FirstAutomationProject/
├── pages/                  # Page Object Model classes
│   └── login_page.py      # Login page objects and methods
├── tests/                  # Test files
│   ├── test_login.py      # Basic login tests
│   └── test_login_with_pages.py  # Tests using page objects
├── utils/                  # Utility functions
├── test_data/             # Test data files
├── reports/               # Generated test reports
├── requirements.txt       # Python dependencies
├── pytest.ini            # PyTest configuration
├── README.md             # Project documentation
└── .gitignore            # Git ignore rules
```

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8 or higher installed
- Google Chrome browser installed
- IntelliJ IDEA (recommended) or any Python IDE

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/FirstAutomationProject.git
   cd FirstAutomationProject
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify installation**
   ```bash
   python -c "import selenium; print('Selenium installed successfully')"
   ```

## ▶️ Running Tests

### Run All Tests
```bash
pytest
```

### Run Specific Test File
```bash
pytest tests/test_login.py
```

### Run Tests with HTML Report
```bash
pytest --html=reports/report.html --self-contained-html
```

### Run Tests in Parallel
```bash
pytest -n 2  # Run with 2 workers
```

### Run Tests with Specific Markers
```bash
pytest -m smoke  # Run only smoke tests
```

## 📊 Test Reports

After running tests, you can find:
- **HTML Reports**: `reports/report.html`
- **Console Output**: Detailed test execution logs
- **Screenshots**: Captured on test failures (if configured)

## 🧪 Test Scenarios Covered

- ✅ Valid login with correct credentials
- ✅ Invalid login with wrong username
- ✅ Invalid login with wrong password
- ✅ Login with empty credentials
- ✅ Login with various invalid combinations (parameterized)

## 📝 Adding New Tests

1. Create new test files in the `tests/` directory
2. Follow the naming convention: `test_*.py`
3. Use Page Object Model for better maintainability
4. Add appropriate assertions and error handling

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📈 Future Enhancements

- [ ] Add API testing capabilities
- [ ] Implement database testing
- [ ] Add mobile automation support
- [ ] Integrate with CI/CD pipelines
- [ ] Add performance testing features
- [ ] Implement AI-powered test generation

## 📞 Contact

Your Name - [your.email@example.com](mailto:your.email@example.com)

Project Link: [https://github.com/yourusername/FirstAutomationProject](https://github.com/yourusername/FirstAutomationProject)

---
⭐ If you found this project helpful, please give it a star!