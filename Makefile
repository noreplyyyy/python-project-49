install: # установка поетри
	poetry install

brain-games: #запуск
	poetry run brain-games

build: #собираем
	poetry build

publish: #публикуем
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl