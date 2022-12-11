from flask import jsonify, make_response

# bad request
def bad_request(description=""):
	return make_response(jsonify({'description':f"{description}",'error': 'Bad Request','status_code':400}), 400)

def success(message, status_code=200):
    return make_response(jsonify({'status_code': status_code, 'message': message}), status_code)