find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
rm ./*/__pycache__/*
rm ./*/migrations/__pycache__/*
rm db.sqlite3