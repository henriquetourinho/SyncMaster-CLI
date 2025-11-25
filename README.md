

# SyncMaster-CLI v1.0 🚀

![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)
![Python](https://img.shields.io/badge/python-3.x-yellow.svg)
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20unix-lightgrey)

<p align="center">
  <a href="#-english">🇺🇸 <strong>English</strong></a> |
  <a href="#-português">🇧🇷 <strong>Português</strong></a>
</p>

---

<div id="english"></div>

## 🇺🇸 English

**Professional Auto-Deploy & Git Sync Tool**

**SyncMaster-CLI** is a standalone Python tool designed to automate the synchronization between local directories and GitHub repositories. Built with **zero external dependencies** (no `pip install` needed), it utilizes only the Python Standard Library to ensure maximum compatibility on any Linux server or workstation.

### 🔥 Key Features

- **🐍 Zero Dependencies:** Runs on pure Python (`os`, `subprocess`, `json`, `time`). Just download and run.
- **🛡️ Smart & Secure:** Detects permission errors (403) and saves your token configuration in a hidden, encrypted-like file with restricted permissions (`chmod 600`).
- **🔧 Self-Healing:** Automatically fixes broken or changed Git Remote URLs.
- **💾 Persistent Config:** Remembers your user, repo, and token for future runs.
- **🖥️ Rich CLI UI:** Professional interface with color-coded logs and progress bars.
- **🔄 Loop Mode:** Set intervals (e.g., every 60s) for continuous background synchronization.

### 📦 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/henriquetourinho/SyncMaster-CLI.git](https://github.com/henriquetourinho/SyncMaster-CLI.git)
   cd SyncMaster-CLI


2.  **Run the tool:**

    ```bash
    python3 SyncMaster-CLI.py
    ```

3.  **Follow the on-screen instructions:**

      - Enter Local Path.
      - Enter GitHub User & Repo.
      - Paste your **Personal Access Token** (Ensure `repo` scope is checked).
      - Set sync interval (or 0 for single run).

-----

\<div id="português"\>\</div\>

## 🇧🇷 Português

**Ferramenta Profissional de Auto-Deploy e Sincronização Git**

O **SyncMaster-CLI** é uma ferramenta *standalone* desenvolvida em Python para automatizar a sincronização entre diretórios locais e repositórios GitHub. Construído com **zero dependências externas** (sem necessidade de `pip install`), ele utiliza apenas a Biblioteca Padrão do Python, garantindo máxima compatibilidade e facilidade de uso em qualquer servidor ou estação de trabalho Linux.

### 🔥 Principais Funcionalidades

  - **🐍 Zero Dependências:** Roda em Python puro (`os`, `subprocess`, `json`, `time`). Basta baixar e usar.
  - **🛡️ Inteligente & Seguro:** Detecta erros de permissão (403) e salva suas configurações de token em arquivo oculto com permissões restritas (`chmod 600`).
  - **🔧 Auto-Correção (Self-Healing):** Corrige automaticamente URLs de Git Remote quebradas ou alteradas.
  - **💾 Configuração Persistente:** Lembra seu usuário, repositório e token para as próximas execuções.
  - **🖥️ Interface CLI Rica:** UI profissional com logs coloridos, tratamento de erros e barras de progresso.
  - **🔄 Modo Loop:** Permite definir intervalos (ex: a cada 60s) para sincronização contínua em background.

### 📦 Instalação e Uso

1.  **Clone o repositório:**

    ```bash
    git clone [https://github.com/henriquetourinho/SyncMaster-CLI.git](https://github.com/henriquetourinho/SyncMaster-CLI.git)
    cd SyncMaster-CLI
    ```

2.  **Execute a ferramenta:**

    ```bash
    python3 SyncMaster-CLI.py
    ```

3.  **Siga as instruções na tela:**

      - Informe o caminho da Pasta Local.
      - Informe seu Usuário e Repositório do GitHub.
      - Cole seu **Personal Access Token** (Certifique-se de marcar a permissão `repo` ao criar o token).
      - Defina o intervalo de sincronização (ou 0 para rodar apenas uma vez).

-----

## 📜 License / Licença

Distributed under the **GNU General Public License v3.0**
Distribuído sob a **Licença Pública Geral GNU v3.0**

🔗 [https://www.gnu.org/licenses/gpl-3.0.html](https://www.gnu.org/licenses/gpl-3.0.html)

-----

## 👨‍💻 Author / Autor

**Carlos Henrique Tourinho Santana**
📍 Salvador – Bahia – Brasil

  * GitHub: [@henriquetourinho](https://github.com/henriquetourinho)
  * LinkedIn: [Carlos Henrique Tourinho Santana](https://br.linkedin.com/in/carloshenriquetourinhosantana)
  * Wiki Debian: [wiki.debian.org/henriquetourinho](https://wiki.debian.org/henriquetourinho)

-----

*Developed with simplicity, security, and efficiency in mind.*


