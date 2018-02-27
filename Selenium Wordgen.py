from datetime import time
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



def mainv1(nicktext):
    browser = webdriver.Chrome()
    browser.get('https://worditout.com/word-cloud/create')
    button = browser.find_element_by_name('paste')
    button.click()
    button.send_keys(nicktext)
    print(button)
    Generate = browser.find_element_by_css_selector(".c.bz.cY.S.bU.eg.cu")
    Generate.click()
    browser.fullscreen_window()
    browser.implicitly_wait(10)
    browser.save_screenshot("nickposting.png")
    im = Image.open('nickposting.png')
    left = 730
    top = 120
    right = 1550
    bottom = 630
    im = im.crop((left,top,right,bottom))
    im.save('nickpostings.png')



def tagcrowdart():
    browser = webdriver.Chrome()
    browser.get('https://tagcrowd.com/')
    button = browser.find_element_by_name('text')
    button.click()
    button.send_keys("NBC’s Katie Couric suggested during coverage of the Opening Ceremony, there is the fact that the Dutch consider speedskating to be “an important mode of transport” over frozen canals. Damn I want to be a news anchor I've given up on wining over any girls in person with my non existent personality, and switched exclusively to tinder. I still have yet to create a profile, not being sure what pics to use. I don't want to just slap something on there but I have no idea what would be a flattering and well thought out shot. I will however include the picture of me making frens with a horse after that in my profile. Laurance, please do not subvert yourself for others pointless causes. A man deserves to live his life, making his own choices, embracing his brothers truly, and loving his family wholeheartedly. This false cause of 'cucks' and 'feminism' is only an effort to steal this from you, to make you fight your brothers and those you love, for the enrichment of the bastards who care not for you or your dreams. Please do not let such things limit you. Do not avoid living your life the best you can out of fear of 'nu-males' and 'degeneracy'. Do not fear to express and live your love because of how those still asleep will view you. The hypothetical men in your pictures are just the same as you. They had dreams, they had wives they loved, but they threw these away because they had been manipulated into seeing no other choice, because they feared, and thus could not think to fight for what is theirs. Just as you fear to share your talent for cooking with the girl you care about, and fear to feel, that you be seen as weak and unmanly. Trust me, none of what others say matters. I've lived for 18 years trying to be something for others, afraid to even have a hobby. This is where such ideologies lead, to being a man who looks back and realizes the happiness  he could have had, and the dreams he's allowed to languish. I know it's hard to wake up to these things, but you'll be a man soon, and hard as it is, finding your desires and pursuing them is what makes a man.")
    print(button)
    Visualize = browser.find_element_by_name('tc_submit')
    Visualize.submit()
    browser.fullscreen_window()
    browser.save_screenshot("nickposting.png")


if __name__ == '__main__':
    file = open('nickposts.txt','r')
    stringaccum = ""
    for line in file:
        temp = line.strip().split(':')
        stringaccum += temp[3]

    mainv1(stringaccum)



