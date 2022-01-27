#!/usr/bin/env python
# coding: utf-8

# In[2]:


pets = {
    'dogs': [
        {
            'name': 'Spot',
            'age': 2,
            'breed': 'Dalmatian',
            'description': 'Spot is an energetic puppy who seeks fun and adventure!',
            'url': 'https://content.codecademy.com/programs/flask/introduction-to-flask/dog-spot.jpeg'
        },
        {
            'name': 'Shadow',
            'age': 4,
            'breed': 'Border Collie',
            'description': 'Eager and curious, Shadow enjoys company and can always be found tagging along at your heels!',
            'url': 'https://content.codecademy.com/programs/flask/introduction-to-flask/dog-shadow.jpeg'
        }
    ],
    'cats': [
        {
            'name': 'Snowflake',
            'age': 1,
            'breed': 'Tabby',
            'description': 'Snowflake is a playful kitten who loves roaming the house and exploring.',
            'url': 'https://content.codecademy.com/programs/flask/introduction-to-flask/cat-snowflake.jpeg'
        }
    ],
    'rabbits': [
        {
            'name': 'Easter',
            'age': 4,
            'breed': 'Mini Rex',
            'description': 'Easter is a sweet, gentle rabbit who likes spending most of the day sleeping.',
            'url': 'https://content.codecademy.com/programs/flask/introduction-to-flask/rabbit-easter.jpeg'
        }
    ]
}


# In[5]:


from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return """<h1>Adopt a Pet!</h1>
                <p>Browse through the links below to find your new furry friend:</p>
                <ul>
                    <li><a href="/animals/dogs">Dogs</a></li>
                    <li><a href="/animals/cats">Cats</a></li>
                    <li><a href="/animals/rabbits">Rabbits</a></li>
                </ul>
            """
@app.route('/animals/<pet_type>')
def animals(pet_type):
    html = "<h1>List of {}</h1>".format(pet_type)
    html += "<ul>"
    html = "<h1>List of {}</h1>".format(pet_type)
    html += "<ul>"

    for pet in pets[pet_type]:
        html += "<li>{n}</li>".format(n = pet["name"])
    for i,pet in enumerate(pets[pet_type]):
        html += "<li><a href='/animals/{}/{}'>{n}</a></li>".format(pet_type,i,n = pet["name"])

    html += "</ul>"


    return html


@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    pet = pets[pet_type][pet_id]
    html = "<h1>{}</h1>".format(pet['name'])
    html += "<img src={}>".format(pet['url'])
    html += "<p>{}</p>".format(pet['description'])
    html += "<ul><li>Breed: {}</li><li>Age: {}</li></ul>".format(pet['breed'], pet['age'])
    return html

if __name__ == "__main__":
    app.run(debug=True,use_reloader=False)


# In[ ]:
