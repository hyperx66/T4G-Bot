import flask, firebase_admin

model1 = "I am model 1"
model2 = "I am model 2"
modelFlag = 0

cred_obj = firebase_admin.credentials.Certificate('....path to file')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':""
	})

def modelFirstRuntime():
    print("Running Model")


def modelSecondRuntime():
    print("Running Model 2")


app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def query():
    if modelFlag == 0:
        return "model 1 launched"
    else:
        return "model 2 launched"

@app.route('/', methods=['POST'])
def insertWords():
    print("")

if __name__ == "__main__":
    print("main runtime")
    app.run()
