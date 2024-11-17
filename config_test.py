import configparser

config = configparser.ConfigParser() #объект для обращения к ini

config.read('settings.ini')

print(config['Telegram']['username'])
print(config['Telegram']['password'])

#создаем новую секцию
config.add_section('VK')
config.set('VK', 'vkuser', 'vk_pass')

with open('settings.ini', 'w', encoding='UTF-8') as f:
    config.write(f)