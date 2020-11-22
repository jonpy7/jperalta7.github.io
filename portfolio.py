from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    # if not name or not email or not message:
    #     return render_template('failure.html')
    return render_template("contact.html", name = name, email = email, message = message)

@app.route('/hotelsite')
def hotelsite():
    return render_template('/Hotel_Website/portfolio-hotel.html')
    
if __name__ == '__main__':
    app.run(debug=True, port=5050)