# TODO：缓存文件
import os

from resources.lib import router, getImg

class Cache():
    def __init__(self, path):
        self.path = os.path.join(path, 'cache')
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        self.screenshot_path = os.path.join(self.path, 'screenshots')
        if not os.path.exists(self.screenshot_path):
            os.mkdir(self.screenshot_path)

    def cache_screenshot(self, account, platform, data):
        game_folder = os.path.join(self.screenshot_path, str(platform) + account)
        if not os.path.exists(game_folder):
            os.mkdir(game_folder)
        screenshot_folder = os.path.join(game_folder, str(data['UTCTime']))
        screenshots = []
        if os.path.exists(screenshot_folder):
            for i in os.listdir(screenshot_folder):
                screenshots.append(os.path.join(screenshot_folder, i))
        else:
            os.mkdir(screenshot_folder)
            for i in data['fileName']:
                content = router.getContent(url=data['url'] + i)
                file_path = os.path.join(screenshot_folder, i)
                open(file_path, 'wb').write(content)
                png_path = getImg.webp2png(file_path)
                os.remove(file_path)
                screenshots.append(png_path)
        return screenshots
