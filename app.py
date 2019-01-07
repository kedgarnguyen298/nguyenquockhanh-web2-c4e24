from flask import Flask, render_template
app = Flask(__name__)

@app.route("/characters")
def characters():
    c_list = [
        {
            "name": "Thanos",
            "image": "https://cdn.images.express.co.uk/img/dynamic/36/590x/Avengers-Infinity-War-ending-Thanos-can-t-use-the-Gauntlet-ever-again-952582.jpg",
            "link": "https://vi.wikipedia.org/wiki/Thanos"
        },
        {
            "name": "Aquaman",
            "image": "https://cdn.images.express.co.uk/img/dynamic/36/590x/Aquaman-preview-screenings-via-Amazon-Prime-1046423.jpg?r=1542390690447",
            "link": "https://vi.wikipedia.org/wiki/Aquaman"
        },
        {
            "name": "Iron man",
            "image": "https://www.firstshowing.net/img/ironman-armor-final-big.jpg",
            "link": "http://asia.ironman.com/#axzz5bjrjhORt"
        }

    ]
    return render_template("characters_list.html", character_list=c_list) 

@app.route("/names")
def name():
    name_list = ["Huy", "Quan", "Khanh", "Huong", "Ha"]
    return render_template("name.html", name_list=name_list) 

food_list = [
        {
            "name": "Che",
            "image": "https://images.foody.vn/res/g10/95877/prof/s640x400/foody-mobile-ghf546-jpg-171-636137015804800853.jpg",
            "link": "https://www.foody.vn/thuong-hieu/ngoc-thach-quan-ha-noi?c=ha-noi",
            "ytid": "tIhdZNqO5fo"
        },
        {
            "name": "Banh trang nuong",
            "image": "https://images.foody.vn/res/g10/94950/prof/s640x400/foody-mobile-cotoan-jpg-374-636088383468583323.jpg",
            "link": "https://www.foody.vn/ha-noi/banh-trang-tron-co-toan",
            "ytid": "wxOqixWL-fs"
        },
        {
            "name": "Chan ga rang muoi",
            "image": "https://images.foody.vn/res/g5/49692/prof/s640x400/foody-mobile-tuga-jpg-466-636147991210200441.jpg",
            "link": "https://www.foody.vn/ha-noi/chan-ga-rang-muoi",
            "ytid": "sNrqgkJp8yg"
        }
    ]

@app.route("/food_items")
def food():   
    return render_template("food.html", food_list=food_list)

@app.route("/food_detail/<int:index>")
def food_detail(index):
    food_item = food_list[index]
    return render_template("food_detail.html", food_item=food_item)


if __name__ == '__main__':
  app.run(debug=True)