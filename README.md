# SyncMaster-CLI v1.0 🚀

![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)
![Python](https://img.shields.io/badge/python-3.x-yellow.svg)
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20unix-lightgrey)

**Ferramenta Profissional de Auto-Deploy e Sincronização Git**

O **SyncMaster-CLI** é uma ferramenta *standalone* desenvolvida em Python para automatizar a sincronização entre diretórios locais e repositórios GitHub. Construído com **zero dependências externas** (sem necessidade de `pip install`), ele utiliza apenas a Biblioteca Padrão do Python, garantindo máxima compatibilidade e facilidade de uso em qualquer servidor ou estação de trabalho Linux.

---

## 🔥 Principais Funcionalidades

- **🐍 Zero Dependências:** Roda em Python puro (`os`, `subprocess`, `json`, `time`). Basta baixar e usar.
- **🛡️ Inteligente & Seguro:** Detecta erros de permissão (403) e salva suas configurações de token em arquivo criptografado/oculto com permissões restritas (`chmod 600`).
- **🔧 Auto-Correção (Self-Healing):** Corrige automaticamente URLs de Git Remote quebradas ou alteradas.
- **💾 Configuração Persistente:** Lembra seu usuário, repositório e token para as próximas execuções.
- **🖥️ Interface CLI Rica:** UI profissional com logs coloridos, tratamento de erros e barras de progresso.
- **🔄 Modo Loop:** Permite definir intervalos (ex: a cada 60s) para sincronização contínua em background.

---

## 📦 Instalação e Uso

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/henriquetourinho/henriquetourinho.git](https://github.com/henriquetourinho/henriquetourinho.git)
   cd henriquetourinho
````

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

## 🛠️ Como Funciona

1.  **Inicialização:** Verifica se a pasta possui `.git`. Se não, inicia o repo e define a branch `main`.
2.  **Configuração:** Configura o `remote origin` com seu token autenticado automaticamente, prevenindo erros de senha.
3.  **Ciclo de Sync:**
      - Verifica mudanças (`git status`).
      - Adiciona arquivos (`git add .`).
      - Realiza commit com timestamp (`git commit`).
      - Baixa atualizações remotas (`git pull --rebase`) para evitar conflitos.
      - Envia para o GitHub (`git push`).

-----

## 📜 Licença

Distribuído sob a **Licença Pública Geral GNU v3.0**
🔗 [https://www.gnu.org/licenses/gpl-3.0.html](https://www.gnu.org/licenses/gpl-3.0.html)

-----

## 👨‍💻 Autor

**Carlos Henrique Tourinho Santana**
📍 Salvador – Bahia – Brasil

  * GitHub: [@henriquetourinho](https://github.com/henriquetourinho)
  * LinkedIn: [Carlos Henrique Tourinho Santana](https://br.linkedin.com/in/carloshenriquetourinhosantana)
  * Wiki Debian: [wiki.debian.org/henriquetourinho](https://wiki.debian.org/henriquetourinho)

-----

*Desenvolvido com foco em simplicidade, segurança e eficiência.*
