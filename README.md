# Yakuza
Django project

## Клонувати собі репозиторій, для роботи з ним
`git clone https://github.com/Denuk68/Yakuza.git`

## Список гілок (branches)
`git branch`

## Переключитись в іншу гілку (branch)
`git chechkout <branchname>`  

## Створити собі гілку для роботи  
`git checkout <основна гілка>`  
`git pull`  
`git branch <своя нова гілка>`  
`git checkout <своя нова гілка>`  
`git push` #створюєм гілку на гітхаб  

## Зберегти зміни і надіслати зміни в гілку 
`git add .` #додали всі змінені файли в індекс  
`git commit -m "message"` #додали коміт  
`git push origin <branch_name>` #закинули на гітхаб  

## Синхронізувати зміни з головної гілки в свою робочу гілку  
Рекомендується робити після кожного змерженого PR в головну гілку.  
Для чого: запобігає конфліктам при наступних Pull Requests з робочої гілки в головну гілку.  

1. Зберегти зміни і надіслати зміни в гілку (див. попередній пункт)
2. `git checkout master`
3. `git pull`
4. `git checkout <своя гілка>`
5. `git merge master` # мержим master собі в гілку
