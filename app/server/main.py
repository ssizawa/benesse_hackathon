from flask import Flask
from flask import render_template, request, jsonify
import similarity
import logging
from sql import sql_arg
SQLARG = sql_arg()

app = Flask(__name__, static_folder='../static', template_folder='../templates')

class User:
    id: int
    name: str
    password: str
    point: int
    list_items: list

class Content:
    title: str
    caption: str
    teature: str
    price: int
    img: str

def get_items_list(myvec):
    formvec_temp=SQLARG.get_form_vec(User.name)
    user_list=[]
    for i in formvec_temp:
        form_vec=[]
        name=i[0]
        q1=i[1]
        
        if q1==None:
            continue
        form_vec.append(q1)
        q2=i[2]
        form_vec.append(q2)
        q3=i[3]
        form_vec.append(q3)
        q4=i[4]
        form_vec.append(q4)
        q5=i[5]
        form_vec.append(q5)
        q6=i[6]
        form_vec.append(q6)
        q7=i[7]
        form_vec.append(q7)
        
        # sim=similarity.cosine_similarity(myvec, form_vec)
        sim=similarity.euclidian(myvec, form_vec)
        form_info={
            'name': name,
            'sim': sim
        }
        user_list.append(form_info)

    sorted_list=sorted(user_list, key=lambda x: x['sim'], reverse=True)
    
    like_user_name=sorted_list[0]['name']
    
    app.logger.setLevel(logging.INFO)
    app.logger.info(like_user_name)

    like_user_info=SQLARG.get_like_user(like_user_name)

    like_movie_list=[]
    for i in like_user_info:
        title=i[0]
        rating=i[1]

        like_movie_dict={
            'title': title,
            'rating': rating
        }
        like_movie_list.append(like_movie_dict)
    
    sorted_like_movie=sorted(like_movie_list, key=lambda x: x['rating'], reverse=True)

    list_items=[]
    rank=0
    for i in sorted_like_movie:
        # app.logger.setLevel(logging.INFO)
        # app.logger.info(i['title'])
        item_temp=SQLARG.get_like_movie(i['title'])
        rank+=1
        for j in item_temp:
            like_title=j[0]
            like_caption=j[1]
            like_teature=j[2]
            like_price=j[3]
            like_img=j[4]
            item_dict={
                'like_rank': rank,
                'like_title': like_title,
                'like_caption': like_caption,
                'like_teature': like_teature,
                'like_price': like_price,
                'like_img': like_img
            }
            app.logger.setLevel(logging.INFO)
            app.logger.info(like_title)
        list_items.append(item_dict)
    return list_items

@app.route('/home', methods=['GET', 'POST'])
def home():
            
    if request.method == "POST":
        myvec=[]
        radio1=request.form['c1']
        myvec.append(int(radio1))
        radio2=request.form['c2']
        myvec.append(int(radio2))
        radio3=request.form['c3']
        myvec.append(int(radio3))
        radio4=request.form['c4']
        myvec.append(int(radio4))
        radio5=request.form['c5']
        myvec.append(int(radio5))
        radio6=request.form['c6']
        myvec.append(int(radio6))
        radio7=request.form['c7']
        myvec.append(int(radio7))

        SQLARG.update_form(User.name, radio1, radio2, radio3, radio4, radio5, radio6, radio7)

        list_items=get_items_list(myvec)
        User.list_items=list_items
        return render_template('index.html',user_name=User.name, list_items=User.list_items, user_point=User.point)
    else:
        return render_template('index.html',user_name=User.name, list_items=User.list_items, user_point=User.point)

@app.route('/')
def main():
    movie_list=SQLARG.get_movie()
    list_items=[]
    for i in movie_list:
        like_title=i[1]
        like_caption=i[2]
        like_teature=i[3]
        like_price=i[4]
        like_img=i[5]
        item_dict={
            'like_title': like_title,
            'like_caption': like_caption,
            'like_teature': like_teature,
            'like_price': like_price,
            'like_img': like_img
        }
        list_items.append(item_dict)
    User.list_items=list_items
    return render_template('login.html')

@app.route('/form')
def form():
    return render_template('form.html', user_name=User.name, user_point=User.point)

@app.route('/set_content', methods=['GET', 'POST'])
def set_content():
    title=request.form['title']
    content_list=SQLARG.get_like_movie(title)
    for j in content_list:
        Content.title=j[0]
        Content.caption=j[1]
        Content.teature=j[2]
        Content.price=j[3]
        Content.img=j[4]
    
    return jsonify({'error' : 'SUCCESS'})
        
@app.route('/content')
def content():
    return render_template('content.html', user_name=User.name,user_point=User.point, title=Content.title, caption=Content.caption, teature=Content.teature, price=Content.price, img=Content.img)

@app.route('/rating', methods=['POST'])
def rating():
    rate=request.form['rate']
    app.logger.setLevel(logging.INFO)
    app.logger.info(rate)
    User.point+=1
    SQLARG.update_point(User.point, User.name)
    return render_template('index.html',user_name=User.name, list_items=User.list_items, user_point=User.point)

@app.route('/login')
def login():
    return render_template('index.html', user_name=User.name, list_items=User.list_items, user_point=User.point)

@app.route('/chart')
def chart():
    return render_template('chart.html', user_name=User.name, list_items=User.list_items, user_point=User.point)

@app.route('/graph')
def graph():
    return render_template('graph.html', user_name=User.name, list_items=User.list_items, user_point=User.point)

@app.route('/verify',methods=['GET','POST'])
def verify():
    user_name=request.form['username']
    user_password=request.form['password']

    password=SQLARG.get_user(user_name, user_password)
    
    if len(password)==0:
        return jsonify({'user_name':'0',
                        'error' : 'ログインできませんでした'})
    else:
        for p in password:
            new_pass=p[0]
            point=p[1]

        if new_pass==user_password:
            User.name=user_name
            User.password=user_password
            User.point=point
            return jsonify({'user_name':User.name,
                            'error' : 'ログインしました'})
        else:
            return jsonify({'user_name':'0',
                            'error' : 'パスワードが間違っています'})

@app.route('/register')
def register():
    return render_template('register.html', judge=1)

@app.route('/add_user', methods=['POST'])
def add_user():
    user_name=request.form['name']
    user_password=request.form['password']

    SQLARG.insert_user(user_name, user_password)

    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)