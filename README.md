Celery Decorator `taskcls` Example
===============

This small project explains, how and why to use [celery-pool-asyncio](https://pypi.org/project/celery-pool-asyncio/) and [celery-decorator-taskcls](https://pypi.org/project/celery-decorator-taskcls/) libraries.

* Free software: Apache Software License 2.0

Structure
--------

There are three entrypoints containing the tasks with the same signatures and doing the same thing, but implemented in different way. Each of them contain two tasks. I want to explain why task inheritance is so important. Just imagine, you have to implement another 3 crawler tasks. You can compare ways and choose the most pretty to extend.


[Way 1: Simple Tasks](https://github.com/kai3341/celery-decorator-taskcls-example/blob/master/step_01_simple_tasks.py)
--------

You can launch worker by following command:

```
celery worker -P celery_pool_asyncio:TaskPool -A step_01_simple_tasks
```

There is no inheritance here. Just imagine -- you have to change behavior of these tasks. For example, you have to check response status code and retry the http request if response status is not equals 200. To reach it, you have to change the code of each task. Then imagine, the number of tasks is not 2, but 10, and you have to change each of them. Did you hear about [The Last Line Effect](https://www.viva64.com/en/b/0260/)? A mistake will definitely be made.

![Code Quality](https://hsto.org/getpro/habr/post_images/df2/7f4/bcd/df27f4bcd139790b322570ee2f48e1ab.png)

*Image source: [PVS-Studio corporate article](https://habr.com/en/company/pvs-studio/blog/472492/)*

[Way 2: Inheritance](https://github.com/kai3341/celery-decorator-taskcls-example/blob/master/step_02_inheritance.py)
--------

You can launch worker by following command:

```
celery worker -P celery_pool_asyncio:TaskPool -A step_02_inheritance
```

It's much better. The same behavior is implemented by the same code. But look to the [bottom of file](https://github.com/kai3341/celery-decorator-taskcls-example/blob/master/step_02_inheritance.py#L47). The Copy-Paste problem is not solved, and there are mistakes will be happened here. The second probles is implementing of one thing (class based task) requires 2 entities -- handler class and launcher function.

![Code Quality](https://import.viva64.com/docx/blog/0644_Haiku_3/image1.png)

*Image source: [PVS-Studio corporate article](https://habr.com/en/company/pvs-studio/blog/461253/)*

[Way 3: The `taskcls` idea](https://github.com/kai3341/celery-decorator-taskcls-example/blob/master/step_03_taskcls_idea.py)
--------

You can launch worker by following command:

```
celery worker -P celery_pool_asyncio:TaskPool -A step_03_taskcls_idea
```

It looks like boilerplate problem has been solved

![Difference](https://camo.githubusercontent.com/86d73c65187de35c988dfa361f007f1b63e1cc52/68747470733a2f2f686162726173746f726167652e6f72672f776562742f6f722f746f2f71642f6f72746f71646964616e62727631647470636231643578647275302e706e67)

You can also pass default `**kwargs` like `bind = True`, timeouts and other via nested class `MetaTask`, which can be also inherited. More about it is available in the [docs](https://pypi.org/project/celery-decorator-taskcls/) and [habrahabr post](https://habr.com/ru/post/470547/).
