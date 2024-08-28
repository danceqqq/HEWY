# HEWY
Here Every Will find Yours ` Temporary working title `

A huge project for me, currently aimed at friends and acquaintances for whom I can make work easier in some places, and in others easier to access files






Road Map Feature 
### Server part

- [x] HomeSpot Api
> [!NOTE]
> In my case, this is the use of two PCs - one is a server, the second and subsequent ones are clients
- [x] Logging console
- [ ] File saved

### Client Part

- [ ] Profile User
- [ ] Chatting Page
- [ ] Steam low price parser
- [ ] Store Page
  - [ ] [Taking orders for clothes](https://pages.github.com/) - spec. @Neshumi
  
### UI Part

- [x] Registration & Login panel
   - [x] Blur Background before log
   - [ ] Country regis
- [ ] Theme
- [ ] Chatting text color choose
- [ ] Emoji
  
### Compatibility Part

- [ ] YouTube prewiev [^1]
[^1]: Quite a crutch system through the use of PIL
- [ ]
  
# Instr
Как запускать

На компьютере с базой данных и API запустите файл server.py командой python server.py.
На компьютере с клиентским приложением запустите файл client_server.py командой python client_server.py.
В поле "Адрес сервера" введите IP-адрес компьютера, на котором запущен сервер.
Примечания

В этом примере используется простая аутентификация с логином и паролем, но вы можете использовать более сложные методы аутентификации.
В этом примере используется простой способ получения данных из базы данных, но вы можете использовать более сложные методы получения данных.
В этом примере используется SQLite как база данных, но вы можете использовать любую другую базу данных, поддерживаемую Flask-SQLAlchemy.
