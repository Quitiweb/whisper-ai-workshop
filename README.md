# Whisper AI Workshop
Utiliza Whisper AI para pasar audio a texto. Pasamos el texto a Chat-GPT y, el resultado que nos devuelve,
lo pasamos a `text-to-speech` de Elevenlabs (antes usábamos Google Cloud, pero cambiamos por motivos de pricing)
y lo reproducimos con `playsound` para mantener una "conversación" por voz con Chat-GPT.


## Configuración inicial
El proyecto se hizo con Python 3.11.3
(se recomienda crear un entorno virtual previamente)
Para instalar las dependencias es necesario ejecutar
```
pip install -r requirements.txt
```

## APIs y API Keys
Son necesarias 1 API Key de OPENAI y otra de ElevenLabs (o un fichero *.json de Google Cloud).
El `OPENAI_API_KEY` y `ELEVEN_API_KEY` irán en un fichero `.env` en nuestra máquina local.
(El fichero `*.json` con la configuración y la API-KEY, irá en la carpeta `media/*.json`)

## Ejecutar el chat
Para ejecutar el chat, hay que lanzar desde consola:
```
python qw-audio-chat.py
```
Si no te funciona, prueba usando "python3" o "py" en lugar de "python" en el comando anterior.

## ¿Problemas?
Solo he probado el chat en mi equipo, así que seguramente puedas encontrar problemas.
En ese caso, por favor, crea un issue aquí en `Github` con el mayor detalle que puedas (versión de python, de paquetes,
mensaje completo de error, etc).
Si eres un ninja y lo solucionas, ¡levanta un Pull Request!
