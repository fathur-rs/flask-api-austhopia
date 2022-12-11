from app_name import app
from flask_cors import CORS
import os
from dotenv import load_dotenv
load_dotenv()

cors = CORS(
            app, 
            resources= {r"/*" : {"origins" : "*"}}
            )

if __name__ == '__main__':
    app.run(host=os.getenv('HOST'), port=os.getenv('PORT'), debug=True)