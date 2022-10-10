Шпаргалка Selenium
____
## Оглавление

- Поиск элемента
  - [Методы поиска элементов](#Методы-поиска-элементов)
  - [Поиск элемента по тексту в ссылке](#Поиск-элемента-по-тексту-в-ссылке)
  - [Поиск элемента по XPATH](#Поиск-элемента-по-XPATH)
- Веб элементы
    - [Checkbox, Radiobutton](#Checkbox,-Radiobutton)
    - [Список (select, option)](#Список-(select,-option))
- Уровень списка 1. Пункт 3.

## Методы поиска элементов

- **find_element(By.ID, value)** — поиск по уникальному атрибуту id элемента. Если ваши разработчики проставляют всем элементам в приложении уникальный id, то вам повезло, и вы чаще всего будет использовать этот метод, так как он наиболее стабильный;
- **find_element(By.CSS_SELECTOR, value)** — поиск элемента с помощью правил на основе CSS. Это универсальный метод поиска, так как большинство веб-приложений использует CSS для вёрстки и задания оформления страницам. Если find_element_by_id вам не подходит из-за отсутствия id у элементов, то скорее всего вы будете использовать именно этот метод в ваших тестах;
- **find_element(By.XPATH, value)** — поиск с помощью языка запросов XPath, позволяет выполнять очень гибкий поиск элементов;
- **find_element(By.NAME, value)** — поиск по атрибуту name элемента;
- **find_element(By.TAG_NAME, value)** — поиск элемента по названию тега элемента;
- **find_element(By.CLASS_NAME, value)** — поиск по значению атрибута class;
- **find_element(By.LINK_TEXT, value)** — поиск ссылки на странице по полному совпадению;
- **find_element(By.PARTIAL_LINK_TEXT, value)** — поиск ссылки на странице, если текст селектора совпадает с любой частью текста ссылки.

____

## Поиск элемента по тексту в ссылке

```python
link = browser.find_element(By.LINK_TEXT, "Degree Symbol in Math")  # по полному соответствию текста
link = browser.find_element(By.PARTIAL_LINK_TEXT, "Math")  #  по подстроке
```
____
## Поиск элемента по XPATH

```python
button = browser.find_element(By.XPATH, "//button[@type='submit']")
button = browser.find_element(By.XPATH, "//button[text()='Submit']")
button = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
```
____
## Checkbox, Radiobutton
По label
```html
<input type="checkbox" id="coding" name="interest" value="coding" checked />
<label for="coding">Coding</label>
```
```html
<input type="radio" id="coding" name="language">
<label for="coding">Java</label>
```

```python
input = browser.find_element(By.CSS_SELECTOR, "[for='coding']")
input.click()
```

По value
```html
<input type="checkbox" id="python" name="python" value="python" checked />
```

```html
<input type="radio" name="language" value="python">
```

```python
input = browser.find_element(By.CSS_SELECTOR, "[value='python']")
input.click()
```

get_attribute

```python
robots_radio = browser.find_element(By.ID, "robotsRule")
robots_checked = robots_radio.get_attribute("checked")
assert robots_checked is None
```
____
## Список (select, option)





