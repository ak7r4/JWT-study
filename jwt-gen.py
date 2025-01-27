import jwt

# set the key
weak_key = "secret"

# set the payload
payload = {
    "sub": "1234567890",
    "name": "John Doe",
    "iat": 1516239022  # Timestamp
}

# Here you change the alhorithm
token = jwt.encode(payload, weak_key, algorithm="HS256")

print("Token JWT:")
print(token)
