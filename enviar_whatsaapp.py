#!/usr/bin/env python3
import webbrowser
import time

# Tenta importar a lista de pacientes do arquivo dados.py
try:
    from dados import pacientes
except ImportError:
    print("ERRO: Arquivo 'dados.py' não encontrado.")
    print("Crie um arquivo dados.py com a lista de pacientes.")
    print("Exemplo: pacientes = [('Nome', 'https://wa.me/55...'), ...]")
    exit(1)

print("Abrindo os chats do WhatsApp...")
print("Serão abertas", len(pacientes), "abas no seu navegador.")
print("Em cada uma, basta clicar em ENVIAR.")
print()
input("Pressione ENTER para começar...")

for nome, link in pacientes:
    print(f"Abrindo chat para: {nome}")
    webbrowser.open(link)
    time.sleep(1.5)

print()
print("Pronto! Todas as abas foram abertas.")
print("Agora é só ir em cada aba e clicar em enviar.")