# 🚕 Urban Routes - Automatización de pruebas de la aplicación web
**Allan Yoltic Godinez Solis cohort 26 – Sprint 8 (TripleTen QA Engineer Bootcamp)**

Este proyecto automatiza una serie de pruebas funcionales sobre el sitio web de **Urban Routes**, una aplicación de solicitud de transporte. La automatización fue realizada utilizando **Selenium WebDriver**, **Pytest** y una arquitectura basada en el patrón **Page Object Model (POM)**.

## 📌 ¿Qué pruebas automatiza?

El proyecto realiza las siguientes acciones de forma automática:

1. Configura una dirección de origen y destino.
2. Selecciona la tarifa "Comfort".
3. Ingresa un número de teléfono.
4. Ingresa el código SMS recibido.
5. Agrega una tarjeta de crédito.
6. Escribe un mensaje personalizado para el conductor.
7. Solicita manta y pañuelos.
8. Pide dos helados.
9. Confirma el viaje y espera a que aparezca la información del conductor.

---

## 🧩 Estructura del proyecto

```

qa-project-urban-routes-es/
│
├── data.py                  # Datos como URL base, número de teléfono, tarjeta, etc.
├── sms\_code\_fetcher.py      # API para obtener el código SMS
├── main.py                  # Archivo principal con pruebas estructuradas en Pytest
├── UrbanRoutesPage.py       # Dependencias del proyecto
└── README.md                # Este archivo :)

````

---

## ⚙️ Requisitos

- Python 3.9+
- Google Chrome instalado
- ChromeDriver (compatible con tu versión de Chrome)

---

## 📦 Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/qa-project-urban-routes-es.git
   cd qa-project-urban-routes-es
````

2. **Crea y activa un entorno virtual** (opcional pero recomendado):

   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # En Windows
   ```

3. **Instala las dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Cómo ejecutar las pruebas

Desde la terminal (dentro del proyecto):

```bash
pytest main.py
```

O bien, desde PyCharm puedes hacer clic derecho sobre `main.py` y seleccionar **"Run 'pytest in main'"**.

---

## 🧪 Tecnologías y herramientas usadas

* **Python**
* **Selenium WebDriver**
* **Pytest**
* **WebDriverWait** (esperas explícitas, evitando `time.sleep`)
* **Page Object Model**

---

## 🙋‍♂️ Créditos

Proyecto desarrollado como parte del bootcamp de QA Automation de **TripleTen**.
Automatización realizada por Allan Yoltic Godinez Solis del cohort 26, con base en las prácticas enseñadas por la instructora Anely Doporto.

---

## 📄 Licencia

Este proyecto es de uso educativo. Puedes reutilizar el código con fines académicos o de práctica.
