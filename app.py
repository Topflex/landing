from landing import app

if __name__ == '__main__':
  from landing.db import db

  db.init_app(app)
  app.run(debug=True)