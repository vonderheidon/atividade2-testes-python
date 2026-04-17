import unittest
import requests


class ApiSpark(unittest.TestCase):
    BASE_URL = "http://localhost:8080/api"

    @classmethod
    def setUpClass(cls):
        try:
            requests.get(f"{cls.BASE_URL}/users/list")
        except requests.exceptions.ConnectionError:
            raise unittest.SkipTest("Erro: O servidor Spark Java não está rodando na porta 8080.")

    def test_ct01_cadastro_sucesso(self):
        payload = {
            "name": "Jefferson de Souza Goncalves",
            "email": "jefferson@teste.com",
            "password": "123456789@"
        }
        response = requests.post(f"{self.BASE_URL}/users/register", json=payload)

        self.assertEqual(response.status_code, 201)
        self.assertIn("salvo com sucesso", response.json())

    def test_ct02_cadastro_nome_invalido(self):
        payload = {
            "name": "Je",
            "email": "erro@teste.com",
            "password": "123456789@"
        }
        response = requests.post(f"{self.BASE_URL}/users/register", json=payload)

        self.assertEqual(response.status_code, 400)
        self.assertIn("O nome deve ter pelo menos 3 caracteres", response.json())

    def test_ct03_cadastro_email_duplicado(self):
        payload = {"name": "User 1", "email": "duplicado@teste.com", "password": "123456789@"}

        requests.post(f"{self.BASE_URL}/users/register", json=payload)
        response = requests.post(f"{self.BASE_URL}/users/register", json=payload)

        self.assertEqual(response.status_code, 400)
        self.assertIn("Email já cadastrado", response.json())

    def test_ct04_login_sucesso(self):
        email = "jefferson2@teste.com"
        password = "123456789@"

        requests.post(f"{self.BASE_URL}/users/register",
                      json={"name": "Login User", "email": email, "password": password})

        payload = {"email": email, "password": password}
        response = requests.post(f"{self.BASE_URL}/login", json=payload)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Login realizado com sucesso", response.json())

    def test_ct05_login_senha_incorreta(self):
        email = "login_erro@teste.com"
        requests.post(f"{self.BASE_URL}/users/register",
                      json={"name": "User", "email": email, "password": "123456789@"})

        payload = {"email": email, "password": "senha_errada"}
        response = requests.post(f"{self.BASE_URL}/login", json=payload)

        self.assertEqual(response.status_code, 401)
        self.assertIn("Senha incorreta", response.json())

    def test_ct06_buscar_usuario_por_id(self):
        email = "id_teste@teste.com"
        requests.post(f"{self.BASE_URL}/users/register",
                      json={"name": "Busca ID", "email": email, "password": "123456789@"})

        users = requests.get(f"{self.BASE_URL}/users/list").json()
        user_id = users[-1]['id']

        response = requests.get(f"{self.BASE_URL}/users/{user_id}")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['email'], email)
        self.assertNotIn('password', response.json())

    def test_ct07_deletar_usuario(self):
        email = "jefferson3@teste.com"
        requests.post(f"{self.BASE_URL}/users/register",
                      json={"name": "Para Deletar", "email": email, "password": "123456789@"})

        users = requests.get(f"{self.BASE_URL}/users/list").json()
        user_id = users[-1]['id']

        response = requests.delete(f"{self.BASE_URL}/users/{user_id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn("removido", response.json())


if __name__ == "__main__":
    unittest.main()