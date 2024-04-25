from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

blog_posts = [
    {'id': 1, 'title': 'Test post', 'content': 'This is a test post for 3 operations'}
]

@app.route('/')
def home():
    return render_template('home.html', posts=blog_posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((post for post in blog_posts if post['id'] == post_id), None)
    return render_template('post.html', post=post)

@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        new_post = {
            'id': len(blog_posts) + 1,
            'title': request.form['title'],
            'content': request.form['content']
        }
        blog_posts.append(new_post)
        return redirect(url_for('home'))
    return render_template('add_post.html')

@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = next((post for post in blog_posts if post['id'] == post_id), None)
    if request.method == 'POST':
        post['title'] = request.form['title']
        post['content'] = request.form['content']
        return redirect(url_for('post', post_id=post_id))
    return render_template('edit_post.html', post=post)

@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    global blog_posts
    blog_posts = [post for post in blog_posts if post['id'] != post_id]
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)