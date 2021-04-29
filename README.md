# MyMagazine News Website

MyMagazine is a WIP News Website, built in Django (backend), using the template [GoodGames](https://themeforest.net/item/goodgames-portal-store-html-gaming-template/17704593).

List of working features:
-
- Index
- News
- Gallery
- Search Feature
- Admin Panel
- Basic Auth
- Subscribe to newsletter
- Pagination

ToDo:
-
- Social Auth
- Mailchimp for newsletter
- Forums
- Reviews
- Store with Stripe
- Chat room for users
- Contact Us page with map and contact info
## Installation

Create a virtualenv:

```bash
virtualenv env
```
Install requirements.txt

```bash
pip install -r requirements.txt
```
Make migrations
```bash
manage.py makemigrations
manage.py migrate
```
Run Django server

```bash
manage.py runserver
```

## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
