import os
import subprocess
import time
import sys
import json
from datetime import datetime

# ==========================================
# CONFIGURAÇÃO VISUAL & UI
# ==========================================
class UI:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

    @staticmethod
    def banner():
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{UI.BLUE}")
        print(r"""
   _____                  __  __           _            
  / ____|                |  \/  |         | |           
 | (___  _   _ _ __   ___| \  / | __ _ ___| |_ ___ _ __ 
  \___ \| | | | '_ \ / __| |\/| |/ _` / __| __/ _ \ '__|
  ____) | |_| | | | | (__| |  | | (_| \__ \ ||  __/ |   
 |_____/ \__, |_| |_|\___|_|  |_|\__,_|___/\__\___|_|   
          __/ |                                         
         |___/      v1.0 - SyncMaster CLI               
        """)
        print(f"{UI.ENDC}")
        # --- CRÉDITOS OFICIAIS ---
        print(f"{UI.CYAN}  Desenvolvedor: Carlos Henrique Tourinho Santana")
        print(f"  Github:        https://github.com/henriquetourinho")
        print(f"  Email:         henriquetourinho@riseup.net{UI.ENDC}\n")

    @staticmethod
    def log(msg, tipo="INFO"):
        timestamp = datetime.now().strftime("%H:%M:%S")
        colors = {
            "INFO": UI.BLUE, "SUCCESS": UI.GREEN, 
            "ERROR": UI.FAIL, "WARN": UI.WARNING, "SYSTEM": UI.HEADER
        }
        color = colors.get(tipo, UI.BLUE)
        print(f"[{timestamp}] {color}{tipo}:{UI.ENDC} {msg}")

    @staticmethod
    def progress_bar(seconds):
        total = seconds
        try:
            for i in range(total, 0, -1):
                percent = 100 - ((i / total) * 100)
                bar_length = 30
                filled = int(bar_length * percent // 100)
                bar = '█' * filled + '-' * (bar_length - filled)
                sys.stdout.write(f"\r[{datetime.now().strftime('%H:%M:%S')}] ⏳ Aguardando: |{UI.CYAN}{bar}{UI.ENDC}| {i}s ")
                sys.stdout.flush()
                time.sleep(1)
            sys.stdout.write("\r" + " " * 80 + "\r")
        except KeyboardInterrupt:
            raise

# ==========================================
# GERENCIADOR DE CONFIGURAÇÃO (SAVE/LOAD)
# ==========================================
class ConfigManager:
    FILE_NAME = ".sync_config.json"

    @staticmethod
    def load():
        if os.path.exists(ConfigManager.FILE_NAME):
            try:
                with open(ConfigManager.FILE_NAME, 'r') as f:
                    return json.load(f)
            except:
                return None
        return None

    @staticmethod
    def save(data):
        try:
            with open(ConfigManager.FILE_NAME, 'w') as f:
                json.dump(data, f, indent=4)
            
            # Segurança: Define permissão 600 (Só dono lê/escreve) no Linux
            if os.name == 'posix':
                os.chmod(ConfigManager.FILE_NAME, 0o600)
            
            UI.log("Configurações salvas com segurança.", "SUCCESS")
        except Exception as e:
            UI.log(f"Não foi possível salvar configurações: {e}", "WARN")

# ==========================================
# LÓGICA DO GIT
# ==========================================
class GitManager:
    def __init__(self, config):
        self.local_path = config['path']
        self.user = config['user']
        self.repo = config['repo']
        self.token = config['token']
        self.branch = "main"
        self.remote_url = f"https://{self.user}:{self.token}@github.com/{self.user}/{self.repo}.git"

    def run(self, command):
        return subprocess.run(command, cwd=self.local_path, shell=True, capture_output=True, text=True)

    def check_health(self):
        if not os.path.exists(self.local_path):
            UI.log(f"Diretório não encontrado: {self.local_path}", "ERROR")
            return False
        
        if not os.path.exists(os.path.join(self.local_path, ".git")):
            UI.log("Inicializando Git...", "WARN")
            self.run("git init")
            self.run(f"git branch -M {self.branch}")
        
        UI.log("Verificando remote...", "SYSTEM")
        self.run("git remote remove origin")
        res = self.run(f"git remote add origin {self.remote_url}")
        
        self.run(f"git config user.name '{self.user}'")
        self.run(f"git config user.email '{self.user}@users.noreply.github.com'")

        if res.returncode == 0:
            UI.log("Conexão remota estabelecida.", "SUCCESS")
            return True
        return False

    def sync(self):
        status = self.run("git status --porcelain")
        if not status.stdout.strip():
            UI.log("Nenhuma alteração pendente.", "INFO")
            return

        UI.log("Alterações detectadas...", "WARN")
        self.run("git add .")
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        commit = self.run(f'git commit -m "Auto-Update: {timestamp}"')
        
        if commit.returncode != 0:
            UI.log(f"Erro Commit: {commit.stderr}", "ERROR"); return

        UI.log("Commit realizado.", "SUCCESS")
        UI.log("Sincronizando (Pull/Push)...", "SYSTEM")
        self.run(f"git pull origin {self.branch} --rebase")
        push = self.run(f"git push origin {self.branch}")

        if push.returncode == 0:
            UI.log("UPLOAD CONCLUÍDO! 🚀", "SUCCESS")
        else:
            self.analyze_error(push.stderr)

    def analyze_error(self, error_msg):
        if "403" in error_msg:
            print(f"\n{UI.FAIL}🚨 ERRO 403 (PERMISSÃO):{UI.ENDC} Token inválido ou sem permissão 'repo'.")
        else:
            print(f"\n{UI.FAIL}Erro Git:{UI.ENDC}\n{error_msg}")

# ==========================================
# MAIN FLOW
# ==========================================
def get_user_input():
    print(f"{UI.BOLD}--- Nova Configuração ---{UI.ENDC}")
    path = input(f"📂 Pasta Local [/root/Laboratorio/upload]: ").strip() or "/root/Laboratorio/upload"
    user = input(f"👤 Usuário GitHub [henriquetourinho]: ").strip() or "henriquetourinho"
    repo = input(f"📦 Repositório [henriquetourinho]: ").strip() or "henriquetourinho"
    repo = repo.replace("https://github.com/", "").replace(".git", "").split("/")[-1]
    
    print(f"{UI.WARNING}🔑 Token (Visível): {UI.ENDC}")
    token = input("> ").strip()
    
    val = input(f"⏱️  Intervalo (segundos) [60]: ").strip()
    intervalo = int(val) if val else 60
    
    return {"path": path, "user": user, "repo": repo, "token": token, "intervalo": intervalo}

def main():
    try:
        UI.banner()
        config = ConfigManager.load()
        usar_salvo = False

        if config:
            print(f"{UI.GREEN}Configuração Salva Encontrada:{UI.ENDC}")
            print(f"  📂 Pasta: {config['path']}")
            print(f"  📦 Repo:  {config['repo']}")
            print(f"  ⏱️  Time:  {config['intervalo']}s")
            
            resp = input(f"\n{UI.BOLD}Deseja usar esta configuração? (S/n): {UI.ENDC}").strip().lower()
            if resp in ['', 's', 'y', 'sim']:
                usar_salvo = True

        if not usar_salvo:
            config = get_user_input()
            if config['token']:
                salvar = input("Deseja salvar esta configuração para a próxima? (S/n): ").lower()
                if salvar in ['', 's', 'y']:
                    ConfigManager.save(config)
        
        if not config or not config.get('token'):
            UI.log("Configuração inválida (sem token).", "ERROR")
            return

        git = GitManager(config)
        print("\n" + "="*50)
        
        if not git.check_health(): return

        while True:
            git.sync()
            if config['intervalo'] == 0: break
            UI.progress_bar(config['intervalo'])

    except KeyboardInterrupt:
        print(f"\n\n{UI.FAIL}🛑 Interrompido.{UI.ENDC}")
    except Exception as e:
        print(f"\n\n{UI.FAIL}💥 Erro: {e}{UI.ENDC}")

if __name__ == "__main__":
    main()