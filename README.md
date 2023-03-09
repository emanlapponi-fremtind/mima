# mindful-masters
skaperdagene

Fra en python 3.10 env:

 ```
 pip install -r requirements.txt
 ````

run server fra `backend`-folderen:

```
uvicorn --reload app:app
```

`POST` til http://127.0.0.1:8000/mood

```
{
	"mood": 0.2,
	"text": "jeg hater sjefen"
}
```

`GET` til `http://127.0.0.1:8000/mean` for å få snitt av mood scores

`GET` til `http://127.0.0.1:8000/text` for å få en random text
