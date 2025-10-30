from flask import Blueprint, render_template, request, redirect, url_for
from services.post_service import PostService

post_bp = Blueprint('post', __name__)

@post_bp.route('/')
def index():
    posts = PostService.get_all_posts()
    return render_template('index.html', posts=posts)

@post_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            PostService.create_post(
                title=request.form['title'],
                content=request.form['content']
            )
            return redirect(url_for('post.index'))
        except Exception as e:
            return f'게시글을 저장하는 중 오류가 발생했습니다: {str(e)}'
    return render_template('create.html')

@post_bp.route('/posts/<int:post_id>')
def detail(post_id):
    post = PostService.get_post_by_id(post_id)
    return render_template('detail.html', post=post)

@post_bp.route('/posts/edit/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    post = PostService.get_post_by_id(post_id)
    
    if request.method == 'POST':
        try:
            PostService.update_post(
                post_id=post_id,
                title=request.form['title'],
                content=request.form['content']
            )
            return redirect(url_for('post.detail', post_id=post_id))
        except Exception as e:
            return f'게시글 수정 중 오류가 발생했습니다: {str(e)}'
    return render_template('create.html', post=post)

@post_bp.route('/posts/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    try:
        PostService.delete_post(post_id)
        return redirect(url_for('post.index'))
    except Exception as e:
        return f'게시글 삭제 중 오류가 발생했습니다: {str(e)}'