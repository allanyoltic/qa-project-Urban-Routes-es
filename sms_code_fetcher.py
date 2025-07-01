import requests
from data import api_base_url

def get_sms_code(phone_number: str) -> str:
    number_encoded = phone_number.replace(' ', '%20').replace('+', '%2B')
    api_url = f"{api_base_url}{number_encoded}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        code_data = response.json()
        code = str(code_data.get("code"))
        print(f"[INFO] Código recibido: {code}")
        return code
    except requests.RequestException as e:
        print(f"[ERROR] No se pudo obtener el código SMS: {e}")
        return ""
    except ValueError:
        print("[ERROR] La respuesta no es un JSON válido.")
        return ""