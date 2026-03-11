# secret-manager

![Node](https://img.shields.io/badge/node-20+-green.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Stars](https://img.shields.io/github/stars/rizalsimb1/secret-manager?style=social)

> A powerful developer CLI toolkit built with Typer and Rich. Automates common development tasks — project scaffolding, environment management, secret handling, and deployment.

## ✨ Features

- ✅ Beautiful terminal UI with Rich tables, progress bars, and syntax highlighting
- ✅ Plugin architecture for extending commands
- ✅ Project scaffolding from templates
- ✅ Environment variable encryption and management
- ✅ Auto-complete for bash, zsh, and fish
- ✅ Cross-platform (macOS, Linux, Windows)

## 🛠️ Tech Stack

`Python 3.11+` • `Typer` • `Rich` • `Click` • `PyYAML` • `cryptography`

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/rizalsimb1/secret-manager.git
cd secret-manager

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Quick Start

```python
# Install
pip install .

# Use
devkit init my-project --template fastapi
devkit env set SECRET_KEY=$(openssl rand -hex 32)
devkit env list
devkit deploy --env staging

```

## 📁 Project Structure

```
secret-manager/
├── src/
│   └── main files
├── tests/
│   └── test files
├── requirements.txt
├── README.md
└── LICENSE
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'feat: add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<p align="center">Made with ❤️ by <a href="https://github.com/rizalsimb1">rizalsimb1</a></p>

