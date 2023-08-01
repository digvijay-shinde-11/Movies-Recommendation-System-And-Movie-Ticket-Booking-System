from RecommendationSystem import recommend
from flask import Flask,redirect,url_for,request,render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/recommendation',methods=['POST'])
def recommendation():
    movie_name = request.form['movie']
    similar_movies = list(recommend(movie_name.lower()))
    print(similar_movies)
    return render_template('recommendation.html',similar_movies=similar_movies,recommend=True)

if __name__=='__main__':
    app.run(debug=True)
