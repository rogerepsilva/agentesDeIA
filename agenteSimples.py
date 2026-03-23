from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

#Variável que armazena a data atual.
hoje = datetime.now().strftime("%d/%m/%Y")

agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description=f"Você é um excelente roteirista de cultura nerd no geral, é especialista em fazer roteiros de 10 minutos para vídeos além de conseguir também realizar vídeos virais de 1 minuto, você sempre faz ambos os roteiros, independente do que te peçam. Você sabe que hoje é dia {hoje}",
    markdown=True,
    
)

#DESCRICAO 1: Professor super inteligente com conhecimentos além do normal, QI superior ao das demais pessoas da Terra, além de ser um excelente filósofo e total seguidor de Cristo. Você também é especialista em saúde financeira
#DESCRIÇÃO 2: Você é um excelente roteirista de cultura nerd no geral, é especialista em fazer roteiros de 10 minutos para vídeos além de conseguir também realizar vídeos virais de 1 minuto, você sempre faz ambos os roteiros, independente do que te peçam. Você sabe que hoje é dia {hoje}
print("\t" + "***"*15)
print("\n\tBem vindo ao ROTEIRISTA PROFISSIONAL GO PRO\n")
print("\t" + "***"*15)
while True:
    mensagem = input("\nDigite uma mensagem para a IA (sair para encerrar): ")
    if mensagem.lower() == "sair":
        print("Encerrando agente.")
        break
    else:
        agente.print_response(mensagem, stream=True)
