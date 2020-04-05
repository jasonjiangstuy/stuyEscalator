from flask import Flask, render_template, session

app = Flask(__name__, static_folder='./static', template_folder='./templates')

app.config.update(TEMPLATES_AUTO_RELOAD=True)

from google.cloud import datastore
import datetime
def resetMaindata():
    key = client.key('Escalators', 1234)
    mainData = datastore.Entity(key, exclude_from_indexes=['created', 'purpose'])
    default = [False, False]
    mainData.update({
        # 'created': datetime.datetime.utcnow(),
        # 'purpose': 'status',
        # up down
        '23': default,
        '24': ['N/A', 'N/A'],
        '35': default,
        '46': default,
        '57': default,
        '68': default,
        '79': default

        # ,'done': False
    })
    client.put(mainData)
    return key

#on startup 
def create_client(project_id):
    return datastore.Client(project_id)

client = create_client('jasontestingke')
mainkey = resetMaindata()

def changeStatus(key, value):
  query = client.get(mainkey)
#   result = query.add_filter('purpose', '=', 'status').fetch()
  if not query:
      raise ValueError(
          'Database does not exist.')

  query[key] = value

  client.put(query) 

def listWorking(): # get the set of working a not working escalators
  query = client.get(mainkey)
  result = query
#   result = query.add_filter('purpose', '=', 'status').fetch()
  if not result:
      raise ValueError(
          'Database does not exist.')

  result = sorted(result.items())
#   print(result)
  index = 0
  final = []
  for i in result: 
    temp = []
    key = i[0]
    try:
        key = key[0] + ' to ' + key[1] # make a more readable table
    except:
        ValueError('Key for database messed up---', key)
    # result[index][0] = 
    temp.append(key)
    value = i[1]
    for i in value:
        if i == 'N/A':
            temp.append(i)
        elif i: # if not False
            temp.append('Working')
        else:
            temp.append('Not Working')
    index += 1
    final.append(temp)
      
  return final

@app.route('/', methods=['GET', 'POST'])
def home():
  final = []
  rulebook = listWorking()
  print(rulebook)
  return render_template(
     'index.html', rulebook=rulebook
  )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3030')