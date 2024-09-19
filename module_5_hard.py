import hashlib
import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def __str__(self):
        return f'Пользователь: {self.nickname}, Возраст: {self.age}'


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return f'Видео: {self.title}, Продолжительность: {self.duration}, 18+: {self.adult_mode}'


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hashed_password = hashlib.sha256(password.encode().hexdigest())
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                print(f'Пользователь {nickname} успешно вошел.')
                return
        print('Неверный логин или пароль.')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f'Пользователь {nickname} зарегистрирован и вошел в систему.')

    def log_out(self):
        print(f'Пользователь {self.current_user.nickname} вышел.')
        self.current_user = None

    def add(self, *new_videos):
        for video in new_videos:
            for v in self.videos:
                if v.title == video.title:
                    print(f'Видео {video.title} уже существует.')
                    return
            self.videos.append(video)
            print(f'Видео {video.title} добавлено.')

    def get_videos(self, keyword):
        result = []
        for video in self.videos:
            if keyword.lower() in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, title):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео.')
            return

        video_to_watch = None
        for video in self.videos:
            if video.title == title:
                video_to_watch = video
                break

        if not video_to_watch:
            print(f'Видео {title} не найдено.')
            return

        if video.adult_mode and self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу.')
            return

        print(f'Начинаем просмотр видео: {video_to_watch.title}')
        while video_to_watch.time_now < video_to_watch.duration:
            video_to_watch.time_now += 1
            print(video_to_watch.time_now, end='')
            time.sleep(1)

        print('\nКонец видео.')
        video_to_watch.time_now = 0


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 10)
v2 = Video('Для чего девушкам парень программист?', 5, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('программист'))

ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

ur.watch_video('Лучший язык программирования 2024 года!')
