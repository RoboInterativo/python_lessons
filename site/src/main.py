from flask import Flask
from faker import Faker
from flask import render_template

# Простая инициализация (английский по умолчанию)


# С локализацией (русские данные)
fake = Faker('ru_RU')


db=[]
for i in range(100):
    a={}
    fullname=fake.name().split()
    last=fullname[0]
    first=fullname[1]
    second= fullname[2]
    a={"first": first,
       "last": last,
       "second": second
      }
    db.append(a)








app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html', db=db)


if __name__ == "__main__":
    app.run(debug=True)
