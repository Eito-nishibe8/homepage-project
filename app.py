from flask import Flask, render_template,request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # flashメッセージ用

@app.route('/')
def home():
    return render_template('index.html')




@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # フォーム入力をセッションに保存
        session['form_data'] = {
            'name': request.form['name'],
            'furigana': request.form['furigana'],
            'phone': request.form['phone'],
            'email': request.form['email'],
            'message': request.form['message']
        }
        return redirect(url_for('confirm'))

    # 「戻るボタン」から来た場合はセッションそのまま、
    # メインやURL直打ちから来た場合はセッション消す！
    if 'form_data' in session and request.referrer and not request.referrer.endswith(url_for('confirm')):
        session.pop('form_data', None)

    # セッションがあればフォームに表示、なければ空
    form_data = session.get('form_data', {})
    return render_template('contact.html', data=form_data)





@app.route('/confirm', methods=['GET', 'POST'])
def confirm():
    if request.method == 'POST':
        form_data = session.get('form_data')
        if not form_data:
            return redirect(url_for('contact'))

        # ここに送信処理（例：メール送信）

        session.pop('form_data', None)
        return redirect(url_for('complete'))

    form_data = session.get('form_data')
    if not form_data:
        return redirect(url_for('contact'))

    return render_template('confirm.html', data=form_data)



@app.route('/complete')
def complete():
    return render_template('complete.html')
    #実際にHTMLテンプレートを表示する



from markupsafe import Markup

@app.template_filter('nl2br')
def nl2br(value):
    return Markup(value.replace("\n", "<br>"))


if __name__ == '__main__':
    app.run(debug=True)





