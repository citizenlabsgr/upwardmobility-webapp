Interactive Webapp to visualize upward mobility across the US at a county level. The [Upward Mobility web application](http://upwardmobility.herokuapp.com/) is built with Django and hosted on Heroku.

This project is used along with a [Streamlit app](https://github.com/citizenlabsgr/upwardmobility) integrated as an iframe. The data referenced and used for this project was collected, cleaned, and merged using Jupyter notebooks located in that same repository.

Project setup:

1. set up virtual environment outside of project
- `python -m venv myvenv` where myvenv can be whatever name you want.

2. `source myvenv/bin/activate`
3.  clone project
 - `git clone https://github.com/citizenlabsgr/upwardmobility-webapp`
4. cd upwardmobility-webapp (go into folder)
5. `pip install -r requirements.txt`
6. `python manage.py migrate`
7. `python manage.py runserver --settings=upwardmobility.local_settings`

If you want to contribute:
- `git pull origin main` to make sure your local version is the most updated version
- `git checkout -b my-descriptive-branch-name` (where you create a descriptive branch name, maybe include your name): e.g. `raca-fix-header`
- when it's done and how you like it, save then run (in the base/root of the directory):
   - `git status` to make sure you are only updating what you intend to
   - `git diff` will show you the differences in detail
   - `git add --all` when you are happy with those changes
   - `git commit -m "message here"`
   - `git push origin my-descriptive-branch-name`

You can then go to GitHub and review the changes by submitting a Pull Request, and ask for review or merge directly.
