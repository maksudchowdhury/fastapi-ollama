# Ollama FastAPI JWT Integration

This project integrates **Ollama** with **FastAPI**, utilizing **JWT (JSON Web Tokens)** for secure API access. It allows you to interact with **Ollama models** by generating responses from models like `tinyllama` and managing chat history, all protected with token-based authentication. For this project I have included a dummy user in the main.py file called fake_user which has,

```bash
username: test
password: testPass
```

## Features

- **List Available Models**: Retrieve a list of models available in Ollama.
- **Generate Responses**: Send prompts to a model and get responses.
- **JWT Authentication**: Secure API routes using JWT tokens.
- **Chat History**: Keep track of previous query-response pairs.

## Requirements

- Python 3.8+
- Ollama (tinyllama)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ollama-fastapi-jwt.git
   cd ollama-fastapi-jwt
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the FastAPI app:

   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

### 1. **List Available Models**

- **Endpoint**: `/showModels`
- **Method**: GET
- **Description**: Fetches the list of available models from Ollama.

```bash
curl -X 'GET' 'http://127.0.0.1:8000/showModels'
```

### 2. **Generate Response from Model**

- **Endpoint**: `/promptllama/`
- **Method**: GET
- **Authorization**: Bearer Token (JWT required)
- **Description**: Sends a query to the `tinyllama` model and returns a response.

```bash
curl -X 'GET' 'http://127.0.0.1:8000/promptllama/{query}' -H 'Authorization: Bearer <your_token>'
```

### 3. **View Chat History**

- **Endpoint**: `/history`
- **Method**: GET
- **Authorization**: Bearer Token (JWT required)
- **Description**: Fetches the history of previous query-response pairs.

```bash
curl -X 'GET' 'http://127.0.0.1:8000/history' -H 'Authorization: Bearer <your_token>'
```

### 4. **User Login and Get Token**

- **Endpoint**: `/token`
- **Method**: POST
- **Description**: Authenticates the user and provides a JWT token.

```bash
curl -X 'POST' 'http://127.0.0.1:8000/token'   -d 'username=test&password=testPass'
```

## Environment Variables

The following environment variables can be configured:

- `SECRET_KEY`: The secret key used to sign JWT tokens (default: `supersecret`).
- `ALGORITHM`: The algorithm used for JWT (default: `HS256`).
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Expiration time for access tokens (default: `30`).

## Usage

1. Start the server with `uvicorn main:app --reload`.
2. Retrieve the token by calling the `/token` endpoint with the default username and password (`test/testPass`).
3. Use the token to make authenticated requests to the API routes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
