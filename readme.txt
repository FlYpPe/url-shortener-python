project info:
  This project is an API to add urls and get shorter and easier alternatives, using the alternatives will redirect to original urls automaticatly.
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