#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pets = {
    'dogs': [
        {
            'id': 0,
            'name': 'Spot',
            'age': 2,
            'breed': 'Dalmatian',
            'description': 'Spot is an energetic puppy who seeks fun and adventure!',
            'url': 'https://content.codecademy.com/programs/flask/introduction-to-flask/dog-spot.jpeg'
        },
        {
            'id': 1,
            'name': 'Shadow',
            'age': 4,
            'breed': 'Border Collie',
            'description': 'Eager and curious, Shadow enjoys company and can always be found tagging along at your heels!',
            'url': 'https://content.codecademy.com/programs/flask/introduction-to-flask/dog-shadow.jpeg'
        }
    ],
    'cats': [
        {
            'id': 0,
            'name': 'Snowflake',
            'age': 1,
            'breed': 'Tabby',
            'description': 'Snowflake is a playful kitten who loves roaming the house and exploring.',
            'url': 'https://content.codecademy.com/programs/flask/introduction-to-flask/cat-snowflake.jpeg'
        }
    ],
    'rabbits': [
        {
            'id': 0,
            'name': 'Easter',
            'age': 4,
            'breed': 'Mini Rex',
            'description': 'Easter is a sweet, gentle rabbit who likes spending most of the day sleeping.',
            'url': 'https://content.codecademy.com/programs/flask/introduction-to-flask/rabbit-easter.jpeg'
        }
    ]
}


# In[ ]:


from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


# In[ ]:


@app.route('/animals/<pet_type>')
def animals(pet_type):
    return render_template('listofpets.html',pet_type=pet_type, pets=pets)


# In[ ]:


@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    pet = pets[pet_type][pet_id]
    return render_template('images.html', pet=pet)


# In[ ]:


if __name__ == "__main__":
    app.run(debug=True,use_reloader=False)
