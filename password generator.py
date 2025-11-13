#!/usr/bin/env python3
# password_gen.py
import random
import string
import argparse

def generate_password(length: int = 12, symbols: bool = True) -> str:
    """Retourne un mot de passe aléatoire."""
    chars = string.ascii_letters + string.digits          # A‑Z a‑z 0‑9
    if symbols:
        chars += string.punctuation                       # !@#$%^&*...
    return ''.join(random.choice(chars) for _ in range(length))

def main() -> None:
    parser = argparse.ArgumentParser(description="Générateur de mots de passe")
    parser.add_argument("-l", "--length", type=int, default=12,
                        help="Longueur du mot de passe (défaut : 12)")
    parser.add_argument("-s", "--no-symbols", action="store_true",
                        help="Ne pas inclure de caractères spéciaux")
    args = parser.parse_args()

    pwd = generate_password(args.length, not args.no_symbols)
    print(pwd)

if __name__ == "__main__":
    main()