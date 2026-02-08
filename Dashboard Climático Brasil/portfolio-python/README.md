🌤️ Dashboard Climático Brasil

Um dashboard interativo de dados climáticos em tempo real, desenvolvido com Flask (Python) no backend e JavaScript + Plotly.js no frontend.

O sistema permite selecionar estados e cidades brasileiras para visualizar:

🌡️ Clima atual
💧 Umidade
🌬️ Velocidade do vento
📊 Previsão de temperatura (24h)
📈 Previsão de umidade (24h)
🌙 Modo escuro (Dark Mode)
🚀 Demonstração

Projeto desenvolvido para fins educacionais e portfólio.

(Adicione aqui o link se fizer deploy no Render/Railway)

🛠️ Tecnologias Utilizadas
Backend

Python 3
Flask
Requests
OpenWeatherMap API
Frontend
HTML5
CSS3 (com variáveis CSS e Dark Mode)
JavaScript (ES6+)
Plotly.js (gráficos interativos)
Fetch API (requisições assíncronas)

📦 Funcionalidades
🔎 Seleção dinâmica de Estado e Cidade

Estados carregados via API interna

Cidades carregadas dinamicamente com base no estado selecionado

🌡️ Clima Atual

Temperatura
Umidade
Pressão atmosférica
Velocidade do vento
Condição climática

📊 Previsão para 24h

Gráfico interativo de temperatura
Gráfico interativo de umidade
Hover detalhado com descrição e emoji

🌙 Dark Mode

Alternância dinâmica de tema
Preferência salva no localStorage

⚡ Performance

Requisições paralelas usando Promise.all
Loading spinner animado
Atualização responsiva dos gráficos

🧠 Arquitetura do Projeto
weather-dashboard/
│
├── main.py
├── templates/
│   └── index.html
├── requirements.txt
└── README.md

Backend (Flask)

/api/states → Lista estados disponíveis

/api/cities/<state> → Lista cidades do estado

/api/city/<city> → Retorna clima atual

/api/forecast/<city> → Retorna previsão de 24h

O backend consome a API da OpenWeatherMap e formata os dados para o frontend.

🔐 Configuração da API Key

O projeto utiliza a API da OpenWeatherMap.

Crie uma conta em:
https://openweathermap.org/api

Gere sua API Key

Configure como variável de ambiente:

Windows:
set OPENWEATHER_API_KEY=sua_chave_aqui

Linux/Mac:
export OPENWEATHER_API_KEY=sua_chave_aqui


No main.py:

import os
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

▶️ Como Executar o Projeto
1️⃣ Clone o repositório
git clone https://github.com/seu-usuario/weather-dashboard.git
cd weather-dashboard

2️⃣ Crie ambiente virtual (opcional mas recomendado)
python -m venv venv
venv\Scripts\activate  # Windows

3️⃣ Instale as dependências
pip install -r requirements.txt

4️⃣ Execute o servidor
python main.py


Acesse em:

http://localhost:5000

📊 Diferenciais Técnicos

Arquitetura REST simples e organizada

Separação clara entre backend e frontend

Uso de requisições assíncronas paralelas

Visualização de dados com biblioteca profissional (Plotly)

Modo escuro com CSS variables

Interface responsiva

Tratamento básico de erros

Código organizado e legível

🎯 Objetivo do Projeto

Este projeto foi desenvolvido para:

Praticar desenvolvimento backend com Flask

Consumir APIs externas

Trabalhar com dados em tempo real

Criar visualizações interativas

Demonstrar habilidades fullstack em portfólio

📈 Possíveis Melhorias Futuras

Deploy em nuvem (Render, Railway ou Fly.io)

Cache para reduzir chamadas à API

Geolocalização automática do usuário

Separação de arquivos JS e CSS em /static

Dockerização

Testes automatizados

👨‍💻 Autor

Rafael Mazzilli

Projeto desenvolvido para fins de aprendizado e portfólio profissional.
