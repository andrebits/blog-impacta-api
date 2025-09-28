from django.urls import path
from .views import posts_list, comments_list, get_post_by_id, get_comment_by_post_id, get_post_by_author, create_post, create_comment, update_post, delete_post, delete_comment, register_user, get_user, change_password, delete_user, get_authors, get_comments_by_author, get_comment_by_id, update_comment, tags_search, posts_by_tag

urlpatterns = [

    # user
    path('user/registration/', register_user, name = 'post_list'), # POST
    path('user/', get_user, name = 'get_user'), # GET
    path('user/change_password', change_password, name = 'change_password'), # PUT
    path('user/delete', delete_user, name = 'delete_user'), # DELETE
    


    # posts
    path('posts/', posts_list, name = 'post_list'), # GET
    path('posts/<int:id>', get_post_by_id, name = 'get_post_by_id'), # GET
    path('posts/author/<str:author>', get_post_by_author, name = 'get_post_by_author'), # GET
    path('posts/tag/', posts_by_tag, name = 'posts_by_tag'), # GET
    
    path('posts/create', create_post, name='create_post'), # POST
    path('posts/update/<int:post_id>/', update_post, name='update_post'), # PATCH
    path('posts/delete/<int:post_id>/', delete_post, name='delete_post'), # DELETE

    # authors
    path('authors/', get_authors, name='get_authors'), # GET


    # comments
    path('comments/', comments_list, name = 'comment_list'), # GET
    path('comments/posts/<int:post_id>/', get_comment_by_post_id, name = 'get_comment_by_post_id'), # GET
    path('comments/<int:id>/', get_comment_by_id, name = 'get_comment_by_id'), # GET
    path('comments/author/<str:author>/', get_comments_by_author, name = 'get_comments_by_author'), # GET
    path('comments/posts/<int:post_id>/create', create_comment, name = 'create_comment'), # POST
    path('comments/update/<int:comment_id>/', update_comment, name = 'update_comment'), # PATCH
    path('comments/delete/<int:comment_id>', delete_comment, name = 'delete_comment'), # DELETE


    # tags
    path('tags/', tags_search, name = 'tags_search'), # GET
]

