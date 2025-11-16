commands:
  start virtual env:
    urlshort\Scripts\activate
  start application:
    uvicorn index:app --reload
  share project:
    pip freeze > requirements.txt
    pip install -r requirements.txt