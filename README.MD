## Запуск тестов

Для запуска тестов используйте следующие команды:

- **Запуск всех тестов**:
  ```
   pytest tests/*.py --alluredir=allure-results 
  ```
- **Формирование Allure отчета **:
  ```
  allure serve allure-results  
  ```
