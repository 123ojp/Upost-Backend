# Upost - Backend
#### A reddit for android class
## Usage
- config the setting.py `Upost/setting.py`
    - Edit `SECRET_KEY`
    - Config the email sender account
- pip install requirements `pip install -r requirements.txt`
- Create Super User
    - `python3 manage.py createsuperuser --username admin --email admin@example.com`
- Do the migrate `python manage.py migrate`
- run! `python3 manage.py runserver 8000`


## APIs
### Account
#### Login
- `/api/user/login` `POST`
    - username
    - password
    - return `token`
#### Register
- `/api/user/register` `POST`
    - `email`
    - `username`
    - return `token` on via Email
- `/api/user/create` `POST`
    - `token`
    - `password`
    - `sex`
- `/api/user/info` `GET`
    - Get user info

### Upost
#### Get Info
- `/api/post/b/` `GET`
    - return All board
- `/api/post/b/<board_id/>` `GET`
    - return Posts on board 
- `/api/post/p/` `GET`
    - return all Post
- `/api/post/p/<post_id>/` `GET`
    - return post info

#### Create & Edit & Delete
##### POST
- `/api/b/<board_id>/create` `POST`
    - `title`
    - `text`
    - Create Post
- `p/<post_id>/del` `GET`
    - Delete Post
- `p/<post_id>/edit` `POST`
    - `title`
    - `text`
    - Edit Post
##### Comment
- `p/<post_id>/create` `POST`
    - `text`
- `p/<comment_id>/del` `GET`
    - Delete comment
- `p/<comment_id>/edit` `POST`
    - `text`
    - Edit comment
#### like unlike 
##### Post
- `p/<post_id>/like`  `GET`
    - like post
- `p/<post_id>/unlike`  `GET`
    - unlike post
- `c/<comment_id>/like` `GET`
    - like comment
- `c/<comment_id>/unlike` `GET`
    - unlike comment

## Technics
- Django
- Django Restful framwork

