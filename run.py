import os
from cookbook import app

# if __name__ == '__main__':   
#     app.run(host=os.environ.get("IP"),
#     port=int(os.environ.get("PORT")),
#     debug=True)

if __name__ == '__main__':
    app.run(debug=True)