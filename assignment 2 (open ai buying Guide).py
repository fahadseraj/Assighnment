import openai
import base64
import requests
import json
import os
from dotenv import load_dotenv

openai.api_key = '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'

url = 'https://juicertopicreviews.com/wp-json/wp/v2/'

load_dotenv()
wp_user = os.getenv('wp_user')
wp_password = os.getenv('wp_password')
wp_credential = f'{wp_user}:{wp_password}'
wp_token = base64.b64encode(wp_credential.encode())
wp_header = {'Authorization': 'Basic ' + wp_token.decode('utf-8')}


def text_render(command):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=command,
        temperature=0,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    choices = response.get("choices")
    dict_text = choices[0]
    text = dict_text.get("text").strip('\n')
    return text


def paragraph_text(text):
    """
    this will create paragraph text
    :param text:
    :return:
    """
    final_text = ''.strip()

    text = text.replace('.', '.--').split('--')
    while '' in text:
        text.remove('')

    return_text1 = f'<!-- wp:paragraph --><p>{final_text.join(text[0: 3]).strip()}</p><!-- /wp:paragraph -->'
    return_text2 = f'<!-- wp:paragraph --><p>{final_text.join(text[3:]).strip()}</p><!-- /wp:paragraph -->'

    return return_text1 + return_text2


def buying_text(text):
    """
    this will create paragraph text
    :param text:
    :return:
    """
    final_text = ''.strip()

    text = text.replace('.', '.--').split('--')
    while '' in text:
        text.remove('')

    return_text1 = f'<!-- wp:paragraph --><p>{final_text.join(text[0: 3]).strip()}</p><!-- /wp:paragraph -->'
    return_text2 = f'<!-- wp:paragraph --><p>{final_text.join(text[3:6]).strip()}</p><!-- /wp:paragraph -->'
    return_text3 = f'<!-- wp:paragraph --><p>{final_text.join(text[6:9]).strip()}</p><!-- /wp:paragraph -->'
    return_text4 = f'<!-- wp:paragraph --><p>{final_text.join(text[9:12]).strip()}</p><!-- /wp:paragraph -->'
    return_text5 = f'<!-- wp:paragraph --><p>{final_text.join(text[12:0]).strip()}</p><!-- /wp:paragraph -->'

    final_return = return_text1 + return_text2 + return_text3
    numb_list = ['1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ', '10. ']
    for y in numb_list:
        final_return = final_return.replace(y, f'</br></br>{y}')
    return final_return


def heading_two(text):
    """
    this will create h2
    :param text:
    :return:
    """
    codes = f'<!-- wp:heading --><h2>{text}</h2><!-- /wp:heading -->'
    return codes


def heading_three(text):
    """
    this will create h3
    :param text:
    :return:
    """
    codes = f'<!-- wp:heading --><h3>{text}</h3><!-- /wp:heading -->'
    return codes


def shortcode_text(text):
    codes = f'<!-- wp:shortcode -->{text}<!-- ' \
            f'/wp:shortcode --> '
    return codes


def ques_ans(text):
    num_list = ['1. ', '2. ', '3. ', '4. ', '5. ']
    for x in num_list:
        text = text.replace(x, '')
    q_list = text.split('\n')
    while '' in q_list:
        q_list.remove('')

    q_dictionary = {}
    for q in q_list:
        answer = text_render(q)
        q_dictionary[q] = answer

    faq = ''

    for key, value in q_dictionary.items():
        h3 = heading_three(key)
        p = paragraph_text(value)
        q_content = h3 + p
        faq += q_content

    return faq


def slugify(text):
    """
    this will return slug
    :param text:
    :return:
    """
    codes = text.strip().lower().replace(' ', '-')
    return codes


def concatenate_contents(*args):
    final_content = ''
    for arg in args:
        final_content += arg
    return final_content


with open('givenkeywordlsit,txt', 'r+') as file:
    readline = file.readlines()
    for keyword in readline:
        title = f'Best {keyword}'
        slug = slugify(keyword)
        introduction = paragraph_text(text_render(f'write a blog introduction on {keyword} in 150 words'))
        shortcode_h2 = heading_two(f'Our Recommended Top {keyword} ')
        shortcode = shortcode_text(f'[amazon bestseller="{keyword}" items="8" template="table"]')
        buying_guide_h2 = heading_two(f'What to consider when Buying {keyword}')
        buying_guide = buying_text(text_render(f'buying guides for {keyword} in 1000 words'))
        faq_h2 = heading_two('Frequently Ask Questions')
        question_answer = ques_ans(text_render(f'Write 5 Questions about {keyword}'))
        conclusion_h2 = heading_two('Final word')
        conclusion = paragraph_text(text_render(f'write a short conclusion or final words on {keyword} in 80 words'))
        article = concatenate_contents(introduction, shortcode_h2, shortcode, buying_guide_h2, buying_guide, faq_h2,
                                       question_answer, conclusion_h2, conclusion)

        post_data = {
            'title': title,
            'content': article,
            'slug': slug,
            'status': 'draft',
            'categories': '4'

        }
        res = requests.post(url + 'posts', json=post_data, headers=wp_header)
        print(res, keyword, 'posted')
