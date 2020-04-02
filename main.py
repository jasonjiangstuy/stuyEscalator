from flask import Flask, render_template, session

app = Flask(__name__, static_folder='./static', template_folder='./templates')

app.config.update(TEMPLATES_AUTO_RELOAD=True)

from google.cloud import datastore

def resetMaindata():
    key = client.key('Escalaters')
    mainData = datastore.Entity(
      key, exclude_from_indexes=['created'])
    default = (False, False)
    mainData.update({
        'created': datetime.datetime.utcnow(),
        
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
    return mainData.key

#on startup 
def create_client(project_id):
    return datastore.Client(project_id)
    
client = create_client('jasontestingke')
maininfo = resetMaindata()

def changeStatus(client, task_id):
    with client.transaction():
        key = client.key('Escalaters', task_id)
        data = client.get(key)

        if not data:
            raise ValueError(
                'Database {} does not exist.'.format(task_id))

        task['done'] = True

        client.put(task)  
def listWorking(): # get the set of working a not working escalators
  pass 



@app.route('/', methods=['GET'])
def home():
  rulebook = listWorking()
  return render_template(
    # 'index.html', rulebook= 
  )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3000')