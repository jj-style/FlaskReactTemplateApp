from flask import Blueprint, render_template, redirect, url_for
from flask import current_app as app

from .forms import PostForm

admin_bp = Blueprint(
    __name__,
    "admin",
    url_prefix="/admin",
    template_folder="app/blueprints/admin/templates",
    static_folder="app/blueprints/admin/static",
)


@admin_bp.route("/add_post", methods=["GET", "POST"])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        print(f"Adding new post {form.title.data}, {form.body.data}")
        app.config["POST_MANAGER"].create_post(
            {"title": form.title.data, "body": form.body.data}
        )
        return redirect(url_for("app.blueprints.admin.admin.posts"))
    return render_template(
        "add_post.html", form=form, title="Create Post", header="Create a Post"
    )


@admin_bp.route("/posts")
def posts():
    posts = app.config["POST_MANAGER"].list_posts()
    return render_template("posts.html", title="Posts", posts=posts, header="Posts")
