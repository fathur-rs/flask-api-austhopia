from app_name import app
from flask_cors import CORS
from dotenv import load_dotenv

cors = CORS(
            app, 
            resources= {r"/*" : {"origins" : "*"}}
            )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')