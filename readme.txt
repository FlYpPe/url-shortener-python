project info:
  database:
    sqlite

commands:
  start virtual env:
    urlshort\Scripts\activate
  start application:
    uvicorn app.main:app --reload
  share project:
    pip freeze > requirements.txt
    pip install -r requirements.txt