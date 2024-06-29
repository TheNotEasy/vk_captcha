from vk_captcha import VkCaptchaSolver
import random, requests

session = requests.Session()  
session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'

solver = VkCaptchaSolver(logging=True)  # use logging=False on deploy
sid = random.randint(122112, 10102012012012)
easy_captcha = False
url = f"https://api.vk.com/captcha.php?sid={sid}&s={int(easy_captcha)}"

answer, accuracy = solver.solve(
    url=url,
    minimum_accuracy=0.33,  # keep solving captcha while accuracy < 0.33
    repeat_count=14,  # if we solved captcha with less than minimum_accuracy, then retry repeat_count times
    session=session  # optional parameter. Useful if we want to use proxy or specific headers
)
print(f"I solved captcha = {answer} with accuracy {accuracy:.4}")
