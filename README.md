# Exemplo de Consumo da API de Usuario e Login

## Como rodar:

Primeiro deve ser criado um ambiente virtual:
```bash
python -m venv venv #windows
#---
python3 -m venv venv #unix
```

Entrar no ambiente virtual:
```bash
. venv/bin/activate #unix
#ou
source venv/bin/activate #unix
#---
. venv/Scripts/activate #windows
```

Instalar as dependencias:
```bash
pip install requirements.txt #windows
#---
pip3 install requirements.txt #unix
```

Para rodar o script atual:
```bash
python3 fluxo_api_spark.py #unix
#---
python fluxo_api_spark.py #windows
```

Entendendo como funciona, agora você deve criar os testes usando a lib nativa de testes do python para isso.
