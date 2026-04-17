import requests
import json

BASE_URL = "http://localhost:8080/api/users"
headers = {'Content-Type': 'application/json'}

def user():
    print("--- Iniciando Consumo da API Usuario ---")

    payload = {
        "name": "Dev Spark",
        "email": "dev@teste.com",
        "password": "senha_secreta_123"
    }
    
    print("\nETAPA 1. Criando usuário")
    res_post = requests.post(f"{BASE_URL}/register", data=json.dumps(payload), headers=headers)
    print(f"Status: {res_post.status_code}")
    print(f"Resposta: {res_post.json()}")

    print("\n\n")
    print("\nETAPA 2. Listando usuários para obter o ID...")
    res_list = requests.get(f"{BASE_URL}/list")
    users = res_list.json()
    
    if not users:
        print("Nenhum usuário encontrado na lista.")
        return

    user_id = users[-1]['id']
    print(f"ID encontrado: {user_id}")

    print("\n\n")
    print(f"\nETAPA 3. Buscando usuário pelo ID: {user_id}")
    res_get_id = requests.get(f"{BASE_URL}/{user_id}")
    print(f"Status: {res_get_id.status_code}")
    if res_get_id.status_code == 200:
        print(f"Dados do Usuário: {res_get_id.json()}")
    else:
        print("Erro ao buscar usuário por ID.")

    print("\n\n")
    print(f"\nETAPA4. Deletando usuário: {user_id}")
    res_del = requests.delete(f"{BASE_URL}/{user_id}")
    print(f"Status: {res_del.status_code}")
    print(f"Resposta: {res_del.json()}")


def login():
    print("\n--- Iniciando Consumo da API Login---")

    payload = {
        "name": "Dev Spark",
        "email": "dev@teste.com",
        "password": "senha_secreta_123"
    }
    
    print("\nCriando usuário")
    res_post = requests.post(f"{BASE_URL}/register", data=json.dumps(payload), headers=headers)
    print(f"Status: {res_post.status_code}")
    print(f"Resposta: {res_post.json()}")
    
    login_data = {
        "email": "dev@teste.com",
        "password": "senha_secreta_123"
    }
    
    res = requests.post("http://localhost:8080/api/login", json=login_data)
    print(f"Login correto: {res.status_code} - {res.json()}")

    print("\n\n")
    login_data["password"] = "senha_errada"
    res = requests.post("http://localhost:8080/api/login", json=login_data)
    print(f"Login errado (esperado 401): {res.status_code} - {res.json()}")



if __name__ == "__main__":
    try:
        user()
        login()
    except requests.exceptions.ConnectionError:
        print("Erro: O servidor Spark Java não está rodando na porta 8080.")
