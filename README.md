For run this hw ->

1 - create venv 
``` text
    python -n venv .venv \
```
or 
``` text
  python3 -m venv .venv
```
2 - activate <br>
---2.1 - Windows 
  ``` text
  .\.venv\Scripts\activate
```
---2.2 - linux \ macos
   ``` text
  source .venv\bin\activate
```
3 - installing poetry 
  ``` text
  pip install poetry
```

4 - installing all libraries
  ``` text
  poetry install
 ```
5 - start fronent in run_front
6 - run backend
---6.1 cd
  ``` text
  cd backend
```
---6.2 run
  ``` text
fastapi run __init__.py
```
7 - go to 
``` text
  http://127.0.0.1:8000/docs
```
( idk why its running on 0.0.0.0 in my pc )
its fastapi Swagger UI 

---7.1 or go to flask endpoint 
  ``` text
  http://127.0.0.1:5000/login
```
8 - Enjoy 
