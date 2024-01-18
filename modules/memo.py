from flask import Blueprint, render_template, request, jsonify

memo_bp = Blueprint('memo', __name__)

memos = []


@memo_bp.route('/memo')
def memo():
    return render_template('memo.html')

@memo_bp.route('/add_memo', methods=['POST'])
def add_memo():
    data = request.get_json()
    memo_text = data['text']
    memos.append(memo_text)
    return jsonify({'success': True, 'message': 'メモが正常に追加されました'})


@memo_bp.route('/get_memos')
def get_memos():
    return jsonify({'memos': memos})
