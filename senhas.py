import random, string 
import sys
sys.stdout.reconfigure(encoding='utf-8')

caracteres = string.ascii_letters +string.digits
senha = "".join(random.choices(caracteres, k=8))
print(f"Sua nova senha é: {senha}")