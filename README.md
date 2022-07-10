# Backend of mayaschool

## How to install the depedencies
```sh
pip install django
pip install pillow
```

## How to config the database
```sh
python manage.py makemigrations
python manage.py migrate
```

# Frontend of mayaschool

## How to install the depedencies
```sh
cd static
mkdir vendor
cd vendor
git clone https://github.com/ColorlibHQ/AdminLTE.git tmp
cp -r tmp/dist adminlte
cp tmp/LICENSE adminlte/LICENSE
cp -r tmp/plugins/* .
rm -rf tmp
```
