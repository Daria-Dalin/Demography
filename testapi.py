from requests import get


print(get('http://127.0.0.1:5000/api/news').json())
print(get('http://127.0.0.1:5000/api/news/1').json())

print(post('http://127.0.0.1:5000/api/news',json={}).json())
print(post('http://127.0.0.1:5000/api/news',
           json={'title': 'Заголовок через API',
                 'content': 'Текст новости',
                 'user_id': 1,
                 'is_private': False
                 }).json())
