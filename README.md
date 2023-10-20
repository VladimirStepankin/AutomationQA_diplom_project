# AutomationQA_diploma_project

# Проект автоматизации тестирования UI для сайта [GoAqua.ru](https://goaqua.ru/)

![GoAqua.jpg](images/logo/GoAqua.jpg)
____

## <a name="Технологии и инструменты">**Технологии и инструменты:**</a>

<br/>
<p align="left">
<a href="https://www.python.org/"><img src="images/logo/Python.png" width="45" height="45"  alt="Python"/></a> 
<a href="https://www.jetbrains.com/pycharm/"><img src="images/logo/pycharm.svg" width="42" height="42"  alt="Pycharm"/></a> 
<a href="https://www.selenium.dev/"><img src="images/logo/selenium-original.svg" width="42" height="42"  alt="Selenium"/></a>
<a href="https://github.com/allure-framework"><img src="images/logo/Allure.png" width="45" height="45"  alt="Allure"/></a>
<a href="https://github.com/"><img src="images/logo/github.svg" width="42" height="42"  alt="Github"/></a>  
</p>

____

## <a name="Начало работы">**Начало работы:**</a>

Github - склонировать проект себе на ПК для последующего запуска и тестирования.

Для запуска тестов на вашем ПК должно быть установлено следующее ПО:

- PyCharm IDEA
- Allure
- Google Chrome (или другой браузер)

---

## <a name="Запуск тестов">**Запуск тестов:**</a>

1. Запускаем авто-тесты командой в терминале:

```
pytest -v --alluredir=tests\allure_results
```

2. Генерируем отчёт по итогам тестирования с помощью Allure. Отчёт автоматически откроется в браузере с помощью команды
   в терминале:

```
allure serve .\tests\allure_results
```

После генерации и работы с отчётом, останавливаем работу allureServe в терминале сочетанием клавиш CTRL + C и
подтверждаем действие в терминале вводом Y.
___

## <img alt="Allure" height="25" src="images/logo/Allure.png" width="25"/></a> <a name="Allure"></a>Allure [отчет](test-documentation/Report.md)</a>

___

### *Основная страница отчёта*

<p align="center">  
<img title="Allure Overview Dashboard" src="скрин" width="850">  
</p>  

### *Тест-кейсы*

<p align="center">  
<img title="Allure Tests" src="скрин2" width="850">  
</p>

### *Графики*

  <p align="center">  
<img title="Allure Graphics" src="граф1" width="850">  
<img title="Allure Graphics" src="граф2" width="850">  
</p>

### <a name="Ссылки на документацию и отчеты:">**Ссылки на документацию и отчеты:**</a>

[План автоматизации тестирования](test-documentation/Plan.md)\
[Отчет о проведенном тестировании](test-documentation/Report.md)\
[Отчет о проведенной автоматизации](test-documentation/Summary.md)

