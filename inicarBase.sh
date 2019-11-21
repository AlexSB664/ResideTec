mysqladmin -h localhost -u root -p drop ResideTec
mysqladmin -h localhost -u root -p create ResideTec
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata > ResideTec/seeds.json
#echo "from superusuario.models import User; User.objects.create_superuser('super@residetec.com', 'super', '123tamarindo')" | python manage.py shell