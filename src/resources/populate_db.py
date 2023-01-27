import datetime

import bs4
import requests
from flask_restful import Resource

from src import db
from src.services.film_service import FilmService
from concurrent.futures.process import ProcessPoolExecutor as PoolExecutor


def converter_time(time: str) -> float:
    hour, minute = time.split('h')
    minutes = (60 * int(hour)) + int(minute.strip('min'))
    return minutes


class PopulateDB(Resource):
    url = 'https://www.imdb.com'

    def post(self):
        t0 = datetime.datetime.now()
        films_urls = self.get_films_urls()
        films = self.parse_films(films_urls)
        created_films = self.populate_db_with_films(films)
        dt = datetime.datetime.now() - t0
        print(f'Done in {dt.total_seconds():.2f} sec.')
        return {'message': f'Database were populated with {created_films} films'}, 201

    def get_films_urls(self):
        print('Getting film urls', flush=True)
        url = self.url + '/chart/top'
        resp = requests.get(url)
        resp.raise_for_status()

        html = resp.text
        soup = bs4.BeautifulSoup(html, features='html.parser')
        movie_containers = soup.find_all('td', class_='posterColumn')
        movie_links = [movie.a.attrs['href'] for movie in movie_containers][:20]
        return movie_links

    def parse_films(self, films_urls):
        headers = {
            'User-Agent': 'Mozilla/5.0'
        }
        film_to_create = []
        for url in films_urls:
            url = self.url + url
            print(f'Getting a detailed info about the film - {url}')
            film_content = requests.get(url, headers=headers)
            film_content.raise_for_status()

            html = film_content.text
            soup = bs4.BeautifulSoup(html, features='html.parser')
            title = soup.find('div', class_='sc-dae4a1bc-0').text.split(':')[1].strip()
            rating_content = soup.find('div', class_='sc-7ab21ed2-2')
            rating = float(rating_content.find('span', {'class': 'sc-7ab21ed2-1'}).get_text())
            description_content = soup.find('p', class_='sc-16ede01-6')
            description = description_content.find('span', class_='sc-16ede01-0').text.strip()
            date = soup.find('span', class_='sc-8c396aa2-2').text.strip()
            release_date = f'01 December {date}'  # for test
            release_date = datetime.datetime.strptime(release_date.strip(), '%d %B %Y')
            length_content = soup.find('div', class_='sc-5be2ae66-2')
            length_content = length_content.find_all('li', class_='ipc-inline-list__item')[-1]
            length = converter_time(length_content.text.strip())
            print(f'Received information about - {title}', flush=True)
            film_to_create.append({
                'title': title,
                'rating': rating,
                'description': description,
                'release_date': release_date,
                'length': length,
                'distributed_by': 'Other distributed'
            })
        return film_to_create

    @staticmethod
    def populate_db_with_films(films):
        return FilmService.bulk_create_films(db.session, films)


class PopulateDBThreadPoolExecutor(Resource):
    url = 'https://www.imdb.com/'

    def post(self):
        t0 = datetime.datetime.now()
        film_urls = self.get_film_urls()
        work = []
        with PoolExecutor() as executor:
            for film_url in film_urls:
                f = executor.submit(self.parse_films, film_url)
                work.append(f)
        films_to_create = [f.result() for f in work]
        created_films = self.populate_db_with_films(films_to_create)

        dt = datetime.datetime.now() - t0
        print(f"Done in {dt.total_seconds():.2f} sec.")

        return {'message': f'Database were populated with {created_films} films.'}, 201

    def get_film_urls(self):
        print('Getting film urls', flush=True)
        url = self.url + 'chart/top/'
        resp = requests.get(url)
        resp.raise_for_status()

        html = resp.text
        soup = bs4.BeautifulSoup(html, features="html.parser")
        movie_containers = soup.find_all('td', class_='posterColumn')
        movie_links = [movie.a.attrs['href'] for movie in movie_containers][:20]

        return movie_links

    def parse_films(self, film_url):
        headers = {
            'User-Agent': 'Mozilla/5.0'
        }
        url = self.url + film_url
        print(f'Getting a detailed info about the film - {url}', flush=True)
        film_content = requests.get(url, headers=headers)
        film_content.raise_for_status()

        html = film_content.text
        soup = bs4.BeautifulSoup(html, features='html.parser')
        title = soup.find('div', class_='sc-dae4a1bc-0').text.split(':')[1].strip()
        rating_content = soup.find('div', class_='sc-7ab21ed2-2')
        rating = float(rating_content.find('span', {'class': 'sc-7ab21ed2-1'}).get_text())
        description_content = soup.find('p', class_='sc-16ede01-6')
        description = description_content.find('span', class_='sc-16ede01-0').text.strip()
        date = soup.find('span', class_='sc-8c396aa2-2').text.strip()
        release_date = f'01 December {date}'  # for test
        release_date = datetime.datetime.strptime(release_date.strip(), '%d %B %Y')
        length_content = soup.find('div', class_='sc-5be2ae66-2')
        length_content = length_content.find_all('li', class_='ipc-inline-list__item')[-1]
        length = converter_time(length_content.text.strip())
        print(f'Received information about - {title}', flush=True)
        return {
            'title': title,
            'rating': rating,
            'description': description,
            'release_date': release_date,
            'length': length,
            'distributed_by': 'Other distributed',
        }

    @staticmethod
    def populate_db_with_films(films):
        return FilmService.bulk_create_films(db.session, films)
