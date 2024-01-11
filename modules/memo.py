from flask import Blueprint, request, render_template, jsonify

app_memo = Blueprint('memo', __name__)


@app_memo.route('/memo')
def memo():
  """
  Route decorator for the '/memo' endpoint.

  Returns:
      A rendered HTML template of 'memo.html'.
  """
  return render_template('memo.html')
