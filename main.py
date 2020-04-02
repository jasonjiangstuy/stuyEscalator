from flask import Flask, render_template, session

app = Flask(__name__, static_folder='./static', template_folder='./templates')

app.config.update(TEMPLATES_AUTO_RELOAD=True)

from google.cloud import datastore

def resetMaindata():
    mainData = datastore.Entity(
      exclude_from_indexes=['created', 'purpose'])
    default = (False, False)
    mainData.update({
        'created': datetime.datetime.utcnow(),
        'purpose': 'status',
        # up down
        '23': default,
        '24': ('N/A'),
        '35': default,
        '46': default,
        '57': default,
        '68': default,
        '79': default

        # ,'done': False
    })
    client.put(mainData)

#on startup 
def create_client(project_id):
    return datastore.Client(project_id)

client = create_client('jasontestingke')
mainkey = resetMaindata()

def changeStatus(key, value):
  query = client.query()
  result = query.add_filter('purpose', '=', 'status').fetch()
  if not data:
      raise ValueError(
          'Database does not exist.')

  result[key] = value

  client.put(result) 

def listWorking(): # get the set of working a not working escalators
  query = client.query()
  result = query.add_filter('purpose', '=', 'status').fetch()
  if not result:
      raise ValueError(
          'Database does not exist.')
  return sorted(result.items())
    

  



@app.route('/', methods=['GET', 'POST'])
def home():
  
  rulebook = listWorking()
  return render_template(
    # 'index.html', rulebook= 
  )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3000')