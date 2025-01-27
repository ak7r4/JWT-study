import jwt
import sys

def crack_jwt(token, wordlist_path, algorithm="HS256"):
    # Open wordlist
    try:
        with open(wordlist_path, 'r') as file:
            words = file.read().splitlines()
    except FileNotFoundError:
        print(f"Erro: Wordlist '{wordlist_path}' not found.")
        return

    total_words = len(words)
    print(f"Key number in wordlist: {total_words}")
    print(f"Using algorithm: {algorithm}")

    # read all lines from wordlist
    for index, word in enumerate(words, start=1):
        try:
            # Print progress
            print(f"Key {index}/{total_words}: {word}")

            # Try crack JWT with the word in wordlist
            decoded = jwt.decode(token, word, algorithms=[algorithm])
            print(f"\nKey found: {word}")
            print("Payload:", decoded)
            return
        except jwt.InvalidTokenError:
            # if wrong word, go to next one
            continue
        except jwt.ExpiredSignatureError:
            # if expired token, but correct key
            print(f"\nKey found: {word} (Token expirado)")
            return
        except Exception as e:
            # invalid token or other errors
            print(f"\nError when proccess token: {e}")
            return

    print("\nKey not found in wordlist.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python crack_jwt.py <JWT_TOKEN> <WORDLIST_PATH> [ALGORITHM]")
        print("Exemplo: python crack_jwt.py <JWT> wordlist.txt HS256")
        sys.exit(1)

    token = sys.argv[1]
    wordlist_path = sys.argv[2]
    algorithm = sys.argv[3] if len(sys.argv) > 3 else "HS256"  # default: HS256

    # supported algorithms
    supported_algorithms = ["HS256", "HS384", "HS512", "RS256", "RS384", "RS512", "ES256", "ES384", "ES512"]

    # verify if is a supported algorithm
    if algorithm not in supported_algorithms:
        print(f"Error: Algorithm '{algorithm}' not supported.")
        print(f"Supported algorithms: {', '.join(supported_algorithms)}")
        sys.exit(1)

    crack_jwt(token, wordlist_path, algorithm)
