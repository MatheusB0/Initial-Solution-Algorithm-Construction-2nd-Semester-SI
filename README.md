# Sistema de Estudos — ODS 4: Educação de Qualidade

Projeto desenvolvido como **solução inicial para o Objetivo de Desenvolvimento Sustentável (ODS) nº 4 — Educação de Qualidade**, na disciplina **Construção de Algoritmos**.

O sistema tem como propósito **facilitar a conexão entre estudantes com interesses em comum**, promovendo colaboração e aprendizado coletivo.

---

## 🎯 Objetivo

Criar uma aplicação simples que:
- Permita o **cadastro e login de estudantes**;
- Guarde informações de forma **segura** (com hash de senha);
- **Encontre parceiros de estudo** com base nas matérias informadas.

---

## ⚙️ Funcionalidades

- Registro de novos usuários;  
- Login com validação de credenciais;  
- Busca de parceiros por matéria;  
- Banco de dados local (SQLite) com persistência automática.  

---

## 🧩 Estrutura do Projeto

```
📂 projeto/
 ├── main.py        # Interface principal e fluxo do sistema
 ├── user.py        # Classe User: registro e autenticação
 ├── sistem.py      # Função para busca de parceiros
 └── data.db        # Banco de dados SQLite (gerado automaticamente)
```

---

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
   cd NOME_DO_REPOSITORIO
   ```

2. Instale as dependências:
   ```bash
   pip install bcrypt
   ```

3. Execute o programa:
   ```bash
   python main.py
   ```

---

## 💡 Exemplo de Uso

```
---Sistema de Estudos---

1 - Registrar
2 - Login
3 - Buscar Parceiro
0 - Sair
```

Exemplo:  
- Cadastrar estudante com matérias: Matemática, Lógica.  
- Buscar parceiros em “Lógica”.  
→ Retorna todos os estudantes que também estudam Lógica.

---

## 🛠️ Tecnologias Utilizadas

- Python 3  
- SQLite3  
- bcrypt  

---

## 🌍 Contribuição para o ODS 4

Este projeto contribui para o ODS 4 — **Educação de Qualidade**, ao:
- Incentivar a colaboração entre estudantes;  
- Criar um ambiente de apoio mútuo no aprendizado;  
- Propor o uso da tecnologia como ferramenta de inclusão educacional.

---

## 📚 Disciplina

- **Construção de Algoritmos**  
- Curso: Sistemas de Informação  

---

## 📄 Licença

Uso livre para fins educacionais e acadêmicos.

---

# Study System — SDG 4: Quality Education

Project developed as an **initial solution for the Sustainable Development Goal (SDG) 4 — Quality Education**, in the **Algorithm Construction** course.

The system aims to **connect students with similar study interests**, encouraging collaboration and shared learning.

---

## 🎯 Goal

Build a simple application that:
- Allows **student registration and login**;  
- Stores data securely (hashed passwords);  
- **Finds study partners** based on subjects of interest.

---

## ⚙️ Features

- User registration  
- Secure login  
- Search for partners by subject  
- Local database using SQLite  

---

## 🧩 Project Structure

```
📂 project/
 ├── main.py        # Main system flow
 ├── user.py        # User class for registration/login
 ├── sistem.py      # Partner search function
 └── data.db        # SQLite database (auto-generated)
```

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/REPOSITORY_NAME.git
   cd REPOSITORY_NAME
   ```

2. Install dependencies:
   ```bash
   pip install bcrypt
   ```

3. Run the system:
   ```bash
   python main.py
   ```

---

## 💡 Example

```
---Study System---

1 - Register
2 - Login
3 - Find Partner
0 - Exit
```

Example:  
- Register a user with subjects: Math, Logic.  
- Search for partners in “Logic”.  
→ Lists users who also study Logic.

---

## 🛠️ Technologies

- Python 3  
- SQLite3  
- bcrypt  

---

## 🌍 Contribution to SDG 4

This project supports **SDG 4: Quality Education** by:
- Promoting collaboration among students;  
- Encouraging mutual learning;  
- Using technology as a tool for educational inclusion.

---

## 📚 Course

- **Algorithm Construction**  
- Degree: Information Systems  

---

## 📄 License

Free for educational and academic use.
