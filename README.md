# Formulário: coleta anônima em Flask

Este projeto fornece um formulário simples (HTML) e backend em Flask que grava respostas em CSV (data/responses.csv).

## Como rodar localmente
1. Criar e ativar um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

2. Instalar dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Rodar a aplicação:
   ```bash
   python app.py
   ```
   Abra http://127.0.0.1:5000/

## Onde os dados são salvos
- As respostas são salvas em `data/responses.csv`.
- Por padrão a pasta `data/` está no `.gitignore` para preservar privacidade. Se você deseja versionar respostas, remova `data/` do `.gitignore` (não recomendado para dados reais).

## Exportar para o repositório
- Copie os arquivos acima para um repositório local.
- Commit e push normalmente:
  ```bash
  git add .
  git commit -m "Adicionar formulário Flask para coleta anônima"
  git push origin main
  ```

Se preferir, eu posso criar os arquivos diretamente em um repositório GitHub — envie o nome `owner/repo` e a branch destino.
