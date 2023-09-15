from django.core.mail import send_mail

def send_activation_code(email, code):
    send_mail(
        'book_store_py29',
        f'Привет перейди по этой ссылке чтобы активировать аккаунт: \n\n'
        f'http://localhost:8000/api/v1/account/activate/{code}',
        'sayansenedwne@gmail.com',
        [email]
    )
